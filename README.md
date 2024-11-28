Personel Takip Sistemi, bir iş yerindeki personel giriş-çıkış verilerini, izin taleplerini ve yıllık izin haklarını yönetmeyi kolaylaştıran bir uygulamadır.
--------------------------------------------------------------------------------------------------------------------
Özellikler
Personel Giriş/Çıkış Takibi: Personellerin çalışma saatlerini kaydedebilir ve bu verileri yöneticiler takip edebilir.
İzin Talepleri ve Onay Süreci: Personeller, yöneticiden onay almak üzere izin talep edebilir ve yöneticiler bu talepleri onaylayabilir veya reddedebilir.
Personel Yönetimi: Yeni personel ekleme, mevcut personel bilgilerini güncelleme veya silme işlemleri yapılabilir.
Aylık Çalışma Süresi Raporu: Personellerin aylık toplam çalışma süresi hesaplanabilir ve raporlanabilir.

Kullanıcılar
Yönetici (Yetkili) Paneli
Yetkili kullanıcılar, personel ekleyebilir, giriş/çıkış verilerini görüntüleyebilir ve izin taleplerini onaylayabilir veya reddedebilir.
Giriş Yaparken: Admin (Süper Kullanıcı) olarak giriş yaptıktan sonra Yetkili Paneli'ne erişebilirsiniz.
Personel Paneli
Personel kullanıcıları, kendi giriş/çıkış kayıtlarını görebilir ve izin taleplerinde bulunabilirler.
Giriş Yaparken: Personel, kendi kullanıcı adı ve şifresi ile giriş yaparak paneline erişebilir.

admin (Süper Kullanıcı) Bilgisi
Admin, uygulamayı yönetebilmek için başlangıçta süper kullanıcı oluşturmak zorundadır. Bunun ardından, Yetkili Paneli üzerinden diğer personelleri ekleyebilir, izin taleplerini onaylayabilir ve diğer yönetimsel işlemleri gerçekleştirebilir.
--------------------------------------------------------------------------------------------------------------------
Bu projede kullanılan teknolojiler:
Django, PostgreSQL, Python 3.13.0 , HTML/CSS, JavaScript, Git, PgAdmin
--------------------------------------------------------------------------------------------------------------------
Proje kurulumu ve çalıştırılma aşamaları
1- git clone https://github.com/AlpGnc/personel_takip.git

Gerekli kütüphaneleri yükleyin: Proje kök dizininde terminal açın ve şu komutu çalıştırarak tüm bağımlılıkları yükleyin:
2- pip install -r requirements.txt


3- Veritabanı bilgilerini kurun
Bu projede PostgreSQL kullanılmaktadır. Aşağıdaki adımları takip ederek veritabanı bağlantısını kurabilirsiniz: (PgAdmin uygulamasını açıp personel_takip adında bir db kurmanız gerekiyor.)

**Veritabanı Bağlantı Bilgileri**:
   DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'personel_takip', #db ismi
        'USER': 'postgres',       #kullanıcı adı bu olmalı
        'PASSWORD': '123',        #şifre
        'HOST': 'localhost',
        'PORT': '5432',
    }
}

Not: Sonuç olarak PgAdmin4 uygulamasında "Servers-PostgreSQL16-DataBases-personel_takip" yolunda oluşturmanız gerekiyor.Kullanıcı adınız uygulamayı kurarken postgres olmalı şifrenizde 123 port ise 5432

4- Veritabanı migrasyonları: Veritabanı tablolarını oluşturmak için:
python manage.py makemigrations
python manage.py migrate

5- Admin (Süper Kullanıcı) Hesabı Oluşturma: Uygulamayı yönetebilmek için bir admin hesabı oluşturun ( Sonrasında Yetkili panelinden tekrar kolayca oluşturabilirsiniz Tek seferlik gerekli):
python manage.py createsuperuser

6- Sunucuyu başlatın: Django uygulamanızı çalıştırmak için:
python manage.py runserver
Tarayıcıda http://127.0.0.1:8000/ adresine giderek uygulamayı kullanabilirsiniz.
--------------------------------------------------------------------------------------------------------------------

A
