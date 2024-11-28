# kullanici/views.py

from django.shortcuts import render, redirect
from .forms import PersonelEkleForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required, user_passes_test

# Yetkili kontrolü
def is_yetkili(user):
    return user.is_authenticated and user.is_yetkili

@login_required
@user_passes_test(is_yetkili)
def personel_ekle(request):
    """
    Yetkili kullanıcıların yeni personel ekleyebileceği view.
    """
    if request.method == 'POST':
        form = PersonelEkleForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Personel başarıyla eklendi!")
            return redirect('saat:yetkili_panel')
        else:
            messages.error(request, "Personel eklenirken bir hata oluştu.")
    else:
        form = PersonelEkleForm()
    return render(request, 'kullanici/personel_ekle.html', {'form': form})
