# saat/utils.py

from django.conf import settings
from datetime import datetime, time, date, timedelta
from django.utils import timezone    
def get_work_start_time():
    """İş başlangıç saatini döndürür."""
    return datetime.strptime(settings.WORK_START_TIME, '%H:%M').time()

def get_work_end_time():
    """İş bitiş saatini döndürür."""
    return datetime.strptime(settings.WORK_END_TIME, '%H:%M').time()

def calculate_lateness(giris_saati):
    """
    İşe geç kalma süresini giriş saatine göre hesaplar.

    :param giris_saati: datetime objesi
    :return: timedelta objesi veya None
    """
    work_start = get_work_start_time()
    start_datetime = datetime.combine(giris_saati.date(), work_start)
    start_datetime = timezone.make_aware(start_datetime, timezone.get_default_timezone())  # Zaman dilimi bilgisi ekle

    if giris_saati > start_datetime:
        lateness = giris_saati - start_datetime
        return lateness
    return None

def is_work_day(check_date):
    """
    Verilen tarihin iş günü olup olmadığını kontrol eder.

    :param check_date: datetime.date objesi
    :return: bool
    """
    return check_date.weekday() < 5  # Pazartesi = 0, ..., Cuma = 4

def calculate_early_exit(cikis_saati):
    """
    İşten erken çıkma süresini hesaplar.

    :param cikis_saati: datetime objesi
    :return: timedelta objesi veya None
    """
    work_end = get_work_end_time()
    cikis_datetime = datetime.combine(cikis_saati.date(), cikis_saati.time())
    end_datetime = datetime.combine(cikis_saati.date(), work_end)
    if cikis_datetime < end_datetime:
        early_exit = end_datetime - cikis_datetime
        return early_exit
    return None