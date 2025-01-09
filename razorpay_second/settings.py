"""
Django settings for razorpay_second project.

Generated by 'django-admin startproject' using Django 5.1.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.1/ref/settings/
"""

from pathlib import Path
# import dj_database_url
# import os

# DATABASES = {
#     'default': dj_database_url.config(default=os.getenv('DATABASE_URL'))
# }
# DATABASES = {
#     'default': dj_database_url.config(
#         default='postgresql://madhu_database_user:1MLLbyQ3MiDiy5582l172POtQPEBQZ6v@dpg-ctv7uulds78s738pgi8g-a.singapore-postgres.render.com/madhu_database?sslmode=require'
#     )
# }
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'madhu_database',  # The database name from the URL
        'USER': 'madhu_database_user',  # The username from the URL
        'PASSWORD': '1MLLbyQ3MiDiy5582l172POtQPEBQZ6v',  # The password from the URL
        'HOST': 'dpg-ctv7uulds78s738pgi8g-a.singapore-postgres.render.com',  # The host from the URL
        'PORT': '5432',  # The default port for PostgreSQL (usually 5432)
        'OPTIONS': {
            'sslmode': 'require',  # Ensuring that SSL is required (from the URL query parameter)
        },
    }
}


# import dj_database_url
# # import environ
# import os
# # import dj_database_url

# DATABASES = {
#     'default': dj_database_url.config(default=os.environ.get('DATABASE_URL'))
# }
# import os
# import dj_database_url

# Get the DATABASE_URL environment variable
# DATABASE_URL = os.environ.get('DATABASE_URL')  # External URL set in Render dashboard

# Parse the DATABASE_URL using dj-database-url
# DATABASES = {
#     'default': dj_database_url.parse("DATABASE_URL")
# }


# DATABASE_URL="postgresql://vmcoffee_database_user:tlACvZfqCcOC8TQLJqOq7a5AkQgUvyDI@dpg-ctunpfl2ng1s739gn7r0-a/vmcoffee_database"

#  import os

# DATABASES = {
#     'default': dj_database_url.config(default=os.getenv('postgresql://djangobackendprojects_user:PZBf6geKtBgX7E17NIv7UvL7F6wpEET6@dpg-cts3o9a3esus73dmkch0-a/djangobackendprojects'))
# }
# DATABASES = {
#     'default': dj_database_url.parse('postgresql://madhu_database_user:1MLLbyQ3MiDiy5582l172POtQPEBQZ6v@dpg-ctv7uulds78s738pgi8g-a.singapore-postgres.render.com/madhu_database?sslmode=require')
# }
# import dj_database_url
# DATABASES = {
#     'default': dj_database_url.parse(
#         'postgresql://madhu_database_user:1MLLbyQ3MiDiy5582l172POtQPEBQZ6v@dpg-ctv7uulds78s738pgi8g-a.singapore-postgres.render.com/madhu_database?sslmode=require'
#     ),
# }

# DATABASE_URL={
#   'default':  dj_database_url.parse('postgresql://vmcoffee_database_user:tlACvZfqCcOC8TQLJqOq7a5AkQgUvyDI@dpg-ctunpfl2ng1s739gn7r0-a/vmcoffee_database')
# }


# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-h*^tw79+7&og5ovk)sx^0+^m3vbbc)!rp86503le5!t1#$#7rm'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'src'
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'razorpay_second.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
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

WSGI_APPLICATION = 'razorpay_second.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.1/ref/settings/#databases

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': BASE_DIR / 'db.sqlite3',
#     }
# }
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql',
#         'NAME': 'vmcoffee_database',
#         'USER': 'vmcoffee_database_user',
#         'PASSWORD': 'tlACvZfqCcOC8TQLJqOq7a5AkQgUvyDI',
#         'HOST': 'mvcoffeeshop.onrender.com',  # e.g., 'localhost' or an IP address, or a URL
#         'PORT': '5432',  # default PostgreSQL port is 5432
#     }
# }



# Password validation
# https://docs.djangoproject.com/en/5.1/ref/settings/#auth-password-validators

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


# Internationalization
# https://docs.djangoproject.com/en/5.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.1/howto/static-files/

STATIC_URL = 'static/'
STATIC_ROOT = BASE_DIR / 'staticfiles'

# Default primary key field type
# https://docs.djangoproject.com/en/5.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


#message sends through emails
EMAIL_HOST= 'smtp.gmail.com'
EMAIL_PORT= 587
EMAIL_HOST_USER= 'vku563786@gmail.com'
EMAIL_HOST_PASSWORD= 'gcmh vrdf qtbn cyko'
EMAIL_USE_TLS=True