"""
Django settings for restaurant project.

Generated by 'django-admin startproject' using Django 3.2.18.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.2/ref/settings/
"""
import os
from pathlib import Path
import dj_database_url
if os.path.isfile('env.py'):
    import env

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent
TEMPLATES_DIR = os.path.join(BASE_DIR, 'templates')

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['restaurant-new-try1.herokuapp.com', 'localhost']

X_FRAME_OPTIONS = 'SAMEORIGIN'

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',

    'django.contrib.sites',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',

    'cloudinary_storage',
    'django.contrib.staticfiles',
    'cloudinary',
    'django_summernote',
    'django_filters',

    'crispy_forms',

    'django.contrib.postgres',

    'home',
    'menu',
    'about',
    'table_booking',
    'users_bookings',
    'contacts',
]

SITE_ID = 1

LOGIN_REDIRECT_URL = '/'
LOGOUT_REDIRECT_URL = '/'

CRISPY_TEMPLATE_PACK = 'bootstrap4'

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'restaurant.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [TEMPLATES_DIR],
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

WSGI_APPLICATION = 'restaurant.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': BASE_DIR / 'db.sqlite3',
#     }
# }

DATABASES = {
    'default': dj_database_url.parse(os.environ.get('DATABASE_URL'))
}

# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

# TIME_ZONE = 'UTC'
TIME_ZONE = 'Europe/Stockholm'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_URL = '/static/'

STATICFILES_STORAGE = 'cloudinary_storage.storage.StaticHashedCloudinaryStorage'
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
DEFAULT_FILE_STORAGE = 'cloudinary_storage.storage.MediaCloudinaryStorage'

# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

ACCOUNT_EMAIL_VERIFICATION = 'none'


# ---------------------------------

# settings.py:

# # Yes, in order to send emails from your Django application, you will need to configure email settings in your project's settings file settings.py. Here's an example of how you can configure email settings using Gmail SMTP:

# # FYI - for contact form 'models.py' is not needed we just want to send this not save it in the database !!! create 'forms.py' and 'urls.py'


# EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'  # this is while in development it needs to be chnaged to Gmail once deploy !!!
# EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
# DEFAULT_FROM_EMAIL = 'testing@example.com'

# EMAIL_HOST = 'smtp.gmail.com'

# EMAIL_PORT = 587 / 1025
# EMAIL_USE_TLS = True / False
# EMAIL_HOST_USER = 'your-gmail-username@gmail.com'
# EMAIL_HOST_PASSWORD = 'your-gmail-password'

# -------------------------------------------------------------------------

# EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
# EMAIL_HOST = '<your_email_host>'
# EMAIL_PORT = <your_email_port>
# EMAIL_USE_TLS = True
# EMAIL_HOST_USER = '<your_email_address>'
# EMAIL_HOST_PASSWORD = '<your_email_password>'


# -------------------------------------------------------------------------
# env.py:

# import os

# os.environ.setdefault('EMAIL_HOST', '<your_email_host>')
# os.environ.setdefault('EMAIL_PORT', '<your_email_port>')
# os.environ.setdefault('EMAIL_HOST_USER', '<your_email_address>')
# os.environ.setdefault('EMAIL_HOST_PASSWORD', '<your_email_password>')

# EMAIL_HOST = os.environ.get('EMAIL_HOST')
# EMAIL_PORT = os.environ.get('EMAIL_PORT')
# EMAIL_HOST_USER = os.environ.get('EMAIL_HOST_USER')
# EMAIL_HOST_PASSWORD = os.environ.get('EMAIL_HOST_PASSWORD')


# # Make sure to replace EMAIL_HOST_USER and EMAIL_HOST_PASSWORD with your own Gmail username and password respectively. You may also need to enable "Less secure app access" for your Gmail account, as Django uses SMTP authentication to send email.

# # Once you have configured your email settings, you can use Django's built-in send_mail function to send the confirmation email to the customer. Here's an example of how you can modify your BookingCreate view to send the confirmation email:


# from django.shortcuts import render, redirect
# from django.core.mail import send_mail, BadHeaderError
# from django.http import HttpResponse, HttpResponseRedirect
# from .forms import ContactForm

# # views.py:
# def send_email(request):
#     if request.method == 'POST':
#         form = ContactForm(request.POST)
#         if form.is_valid():
#             name = form.clean_data['name']
#             phone = form.clean_data['phone']
#             from_email = form.clean_data['from_email']
#             message = form.clean_data['message']

#             try:
#                 send_mail(name, phone, message, from_email, ['admin@example.com'])

#             except BadHeaderError:
#                 return HttpResponse('invalid header')

#             return redirect('contact:send_success')  # contact is from the main url, the 'namespace' added to urls

#     else:
#         form = ContactForm()

#     context = {
#         'form': form
#     }

#     return render(request, 'contact.html', context)


# def send_success(request):
#     return HttpResponse('Thank you for your email ^_^ :D xD')


# class BookingCreate(LoginRequiredMixin, CreateView):
#     # ...

#     def form_valid(self, form):
#         # ...

#         # Send confirmation email to the customer
#         send_mail(
#             'Booking Confirmation',
#             f'Thank you for booking a table at our restaurant. Your booking details are:\n\nTable: {table}\nDate: {date}\nTime: {time}\nNumber of people: {number_of_people}\n\nWe look forward to seeing you!',
#             'from@example.com',
#             [form.instance.customer_email],
#             fail_silently=False,
#         )

#         return super().form_valid(form)



# Additionally, there are several third-party packages available for Django that provide additional functionality for working with templates. For example, the django-crispy-forms package allows developers to easily create and customize forms using pre-built templates, while the django-bootstrap4 package provides a set of Bootstrap 4 templates and tools for use in Django projects.


## Django search q = complex lookups
# from django.db.models import Q

# add it in 'views.py'
## search
# search_query = request.GET.get('q')   This q need to be in our HTML as "name='q'" placed by classes and rest
# if search_query:
#     post_list = post_list.filter(
#         Q(title__icontains = query)   # only one = sign and the query is actually search_query
#         Q(content__icontains = query)
#         Q(tag__name__icontains = query)
#     ).DISTINCT().  ## REMOVES DUPLICATES
# HTML search-form needs to have a METHOD= GET, and a "value={{request.GET.q}}"



## pip3 install django-bootstrap4   or CRISPY
## SummerNote

## Admin page changes
# admin.site.site_header = 'Restaurant AdminPanel'
# admin.site.site_title = 'Restaurant App Admin'
# admin.site.site_index_title = 'Welcome to Restaurant Admin Panel'
