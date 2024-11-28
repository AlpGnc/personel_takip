# saat/views.py

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required, user_passes_test
from django.utils import timezone
from django.contrib import messages
from .models import GirisCikisKayit
from izin.models import Izin
from kullanici.models import Kullanici
from kullanici.forms import PersonelEkleForm
from .forms import GirisCikisForm


def is_yetkili(user):
    return user.is_authenticated and user.is_yetkili


@user_passes_test(is_yetkili)
def yetkili_panel(request):
    """
    Yetkili kullanıcılar için kontrol paneli:
    - Giriş/Çıkış kayıtları
    - İzin talepleri
    - Yeni personel ekleme
    - Personel silme
    """
    giris_cikis_kayitlari = GirisCikisKayit.objects.all()
    izin_talepleri = Izin.objects.filter(onay_durumu='Bekliyor')
    onaylanan_izinler = Izin.objects.filter(onay_durumu='Onaylandı')
    suan_izinli = Izin.objects.filter(onay_durumu='Onaylandı', bitis_tarihi__gte=timezone.now().date())
    personel_listesi = Kullanici.objects.all()

    if request.method == 'POST':
        # Personel Silme İşlemi
        if 'sil' in request.POST:
            personel_id = request.POST.get('sil')
            try:
                personel = Kullanici.objects.get(id=personel_id)
                if not personel.is_superuser:  # Superuser'ı koruma
                    personel.delete()
                    messages.success(request, f"{personel.username} adlı kullanıcı başarıyla silindi.")
                else:
                    messages.error(request, "Superuser kullanıcı silinemez.")
            except Kullanici.DoesNotExist:
                messages.error(request, "Silmek istediğiniz kullanıcı bulunamadı.")
            return redirect('saat:yetkili_panel')

        # İzin Onaylama/Reddetme İşlemi
        elif 'onayla' in request.POST or 'reddet' in request.POST:
            izin_id = request.POST.get('onayla') or request.POST.get('reddet')
            try:
                izin = Izin.objects.get(id=izin_id)
                if 'onayla' in request.POST:
                    # İzin günlerini hesapla
                    izin_gun_sayisi = (izin.bitis_tarihi - izin.baslangic_tarihi).days + 1
                    if izin.personel.annual_leave_balance >= izin_gun_sayisi:
                        izin.onay_durumu = 'Onaylandı'
                        izin.personel.annual_leave_balance -= izin_gun_sayisi
                        izin.personel.save()
                        messages.success(request, f"{izin.personel.username} adlı personelin izin talebi onaylandı. {izin_gun_sayisi} gün izin düştü.")
                    else:
                        messages.error(request, f"{izin.personel.username} adlı personelin yeterli yıllık izin hakkı yok.")
                elif 'reddet' in request.POST:
                    izin.onay_durumu = 'Reddedildi'
                    messages.success(request, f"{izin.personel.username} adlı personelin izin talebi reddedildi.")
                izin.save()
            except Izin.DoesNotExist:
                messages.error(request, "İlgili izin talebi bulunamadı.")
            return redirect('saat:yetkili_panel')

        # Personel Ekleme İşlemi
        elif 'personel_ekle_form' in request.POST:
            form = PersonelEkleForm(request.POST)
            if form.is_valid():
                form.save()
                messages.success(request, "Personel başarıyla eklendi!")
            else:
                messages.error(request, "Personel eklenirken bir hata oluştu.")
            return redirect('saat:yetkili_panel')

        # Giriş/Çıkış Kayıtlarını Temizleme İşlemi
        elif 'temizle_giris_cikis' in request.POST:
            GirisCikisKayit.objects.all().delete()
            messages.success(request, "Tüm giriş/çıkış kayıtları temizlendi.")
            return redirect('saat:yetkili_panel')

    form = PersonelEkleForm()

    context = {
        'giris_cikis_kayitlari': giris_cikis_kayitlari,
        'izin_talepleri': izin_talepleri,
        'onaylanan_izinler': onaylanan_izinler,
        'suan_izinli': suan_izinli,
        'personel_listesi': personel_listesi,
        'personel_ekle_form': form,
    }
    return render(request, 'saat/yetkili_panel.html', context)


@login_required
def redirect_user(request):
    """
    Kullanıcı giriş yaptıktan sonra yetkisine göre yönlendirilir.
    """
    if request.user.is_yetkili:
        return redirect('saat:yetkili_panel')  # Namespace kullanarak yetkili paneline yönlendirme
    return redirect('saat:personel_panel')  # Namespace kullanarak personel paneline yönlendirme


@login_required
def personel_panel(request):
    """
    Personel paneli: giriş/çıkış kayıtları ve izin talepleri
    """
    giris_cikis_kayitlari = GirisCikisKayit.objects.filter(personel=request.user)
    izin_talepleri = Izin.objects.filter(personel=request.user)

    # En son giriş/çıkış kaydını kontrol et
    son_kayit = giris_cikis_kayitlari.last()
    giris_izin_var = not son_kayit or son_kayit.cikis_saati is not None

    # Giriş Kaydı Ekleme
    if request.method == 'POST' and 'giris_kaydi_ekle' in request.POST:
        if giris_izin_var:  # Eğer çıkış yapılmışsa veya hiç giriş yoksa
            GirisCikisKayit.objects.create(personel=request.user)
            messages.success(request, "Giriş kaydı başarıyla eklendi!")
        else:
            messages.error(request, "Yeni bir giriş kaydı eklemeden önce çıkış kaydı eklemeniz gerekiyor.")
        return redirect('saat:personel_panel')

    # Çıkış Kaydı Ekleme
    if request.method == 'POST' and 'cikis_kaydi_ekle' in request.POST:
        if not giris_izin_var:  # Eğer çıkış yapılmamış bir giriş varsa
            form = GirisCikisForm(request.POST)
            if form.is_valid():
                son_kayit.cikis_saati = form.cleaned_data['cikis_saati']
                son_kayit.save()
                messages.success(request, "Çıkış kaydı başarıyla eklendi!")
            else:
                messages.error(request, "Çıkış kaydı eklenirken bir hata oluştu.")
        else:
            messages.error(request, "Çıkış kaydı eklemek için önce bir giriş kaydı eklemelisiniz.")
        return redirect('saat:personel_panel')

    # İzin Talep Etme
    if request.method == 'POST' and 'izin_talep_form' in request.POST:
        baslangic_tarihi = request.POST.get('baslangic_tarihi')
        bitis_tarihi = request.POST.get('bitis_tarihi')
        if baslangic_tarihi and bitis_tarihi:
            Izin.objects.create(
                personel=request.user,
                baslangic_tarihi=baslangic_tarihi,
                bitis_tarihi=bitis_tarihi,
            )
            messages.success(request, "İzin talebiniz başarıyla gönderildi!")
        else:
            messages.error(request, "Başlangıç ve bitiş tarihleri zorunludur.")
        return redirect('saat:personel_panel')

    form = GirisCikisForm()

    context = {
        'giris_cikis_kayitlari': giris_cikis_kayitlari,
        'izin_talepleri': izin_talepleri,
        'form': form,
        'giris_izin_var': giris_izin_var,
    }
    return render(request, 'saat/personel_panel.html', context)
