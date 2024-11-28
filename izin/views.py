# izin/views.py

from django.shortcuts import render, redirect
from .models import Izin
from django.contrib.auth.decorators import login_required

@login_required
def izin_talep_et(request):
    if request.method == 'POST':
        baslangic_tarihi = request.POST.get('baslangic_tarihi')
        bitis_tarihi = request.POST.get('bitis_tarihi')
        Izin.objects.create(
            personel=request.user,
            baslangic_tarihi=baslangic_tarihi,
            bitis_tarihi=bitis_tarihi,
        )
        return redirect('izin:izin_talep_et')
    return render(request, 'izin/izin_talep_et.html')

@login_required
def izin_onayla(request):
    if not request.user.is_yetkili:
        return redirect('homepage')
    izinler = Izin.objects.filter(onay_durumu='Bekliyor')
    return render(request, 'izin/izin_onayla.html', {'izinler': izinler})
