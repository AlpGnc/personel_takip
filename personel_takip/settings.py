# personel_takip/settings.py

from pathlib import Path

# Temel Dizini (Base Directory)
BASE_DIR = Path(__file__).resolve().parent.parent

# Gizli Anahtar (Secret Key)
SECRET_KEY = 'django-insecure-your-secret-key'

# Debug (Hata Ayıklama) Durumu
DEBUG = True

# İzin Verilen Hostlar
ALLOWED_HOSTS = []

# Yüklü Uygulamalar (Installed Apps)
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'kullanici',
    'saat',
    'izin',  # İzin uygulaması
]

# Middleware (Ara Katmanlar)
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# Ana URL Yapılandırması (Root URL Configuration)
ROOT_URLCONF = 'personel_takip.urls'

# Şablonlar (Templates)
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

# WSGI Uygulaması
WSGI_APPLICATION = 'personel_takip.wsgi.application'

# ASGI Uygulaması
ASGI_APPLICATION = 'personel_takip.asgi.application'

# Veritabanı (Database)
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'personel_takip',  # Veritabanı adını buraya girin
        'USER': 'postgres',        # PostgreSQL kullanıcı adınızı buraya girin
        'PASSWORD': '123',         # PostgreSQL şifrenizi buraya girin
        'HOST': 'localhost',
        'PORT': '5432',
    }
}

# Şifre Doğrulayıcıları (Password Validators)
AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# Yerelleştirme (Localization)
LANGUAGE_CODE = 'tr'
TIME_ZONE = 'Europe/Istanbul'
USE_I18N = True
USE_L10N = True
USE_TZ = True

# Statik Dosyalar (Static Files)
STATIC_URL = '/static/'
STATICFILES_DIRS = [BASE_DIR / 'static']

# Varsayılan Birincil Anahtar Alanı Türü
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Özel Kullanıcı Modeli (Custom User Model)
AUTH_USER_MODEL = 'kullanici.Kullanici'

# Giriş Yönlendirmeleri
LOGIN_REDIRECT_URL = 'saat:redirect_user'  # Namespace kullanarak yönlendirme
LOGOUT_REDIRECT_URL = 'homepage'  # Anasayfaya yönlendirme

# Şirket İş Saatleri
WORK_START_TIME = '08:00'
WORK_END_TIME = '18:00'

# Celery Ayarları
CELERY_BROKER_URL = 'redis://localhost:6379/0'
CELERY_RESULT_BACKEND = 'redis://localhost:6379/0'
CELERY_ACCEPT_CONTENT = ['json']
CELERY_TASK_SERIALIZER = 'json'
CELERY_RESULT_SERIALIZER = 'json'

# Django Channels Ayarları
ASGI_APPLICATION = 'personel_takip.asgi.application'

# E-posta Ayarları (Bildirimler için)
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'  # Örneğin Gmail SMTP
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'your_email@example.com'  # E-posta adresinizi buraya girin
EMAIL_HOST_PASSWORD = 'your_email_password'  # E-posta şifrenizi buraya girin

# Admin E-posta Adresleri
ADMINS = [
    ('Admin Name', 'admin@example.com'),
]

DEFAULT_FROM_EMAIL = 'no-reply@example.com'
