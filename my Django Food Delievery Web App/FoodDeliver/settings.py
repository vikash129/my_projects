from pathlib import Path
import os 
BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = 'django-insecure-q@d2kuvql&1*^bl@bg*2o((@&=+0fgy1dl-h(d+yib(o()gv=^'
DEBUG = True
ALLOWED_HOSTS = ["*"]

# for authentication with backend
AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend',
    'allauth.account.auth_backends.AuthenticationBackend',
]


INSTALLED_APPS = [
    'restaurent',
    'customer',

   'crispy_forms',
   
    'allauth',
    'allauth.account',
    'allauth.socialaccount',

     # ... include the providers you want to enable:
    'allauth.socialaccount.providers.amazon',
    'allauth.socialaccount.providers.google',
    # 'allauth.socialaccount.providers.agave',
    #     'allauth.socialaccount.providers.facebook',
    #     'allauth.socialaccount.providers.microsoft',
    #      'allauth.socialaccount.providers.telegram',
    #        'allauth.socialaccount.providers.vk',


    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

SITE_ID = 1



# Provider specific settings
SOCIALACCOUNT_PROVIDERS = {
    'google': {
          'APP': {
            'client_id': '123',
            'secret': '456',
            'key': ''
        } ,
        'SCOPE': [
            'profile',
            'email',
        ],
        'AUTH_PARAMS': {
            'access_type': 'online',
        },
        'OAUTH_PKCE_ENABLED': True,
    }
}

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'FoodDeliver.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR , 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',

                # `allauth` needs this from django
                'django.template.context_processors.request',

                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'FoodDeliver.wsgi.application'



DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

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



LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.0/howto/static-files/

STATIC_URL = '/static/'
STATIC_DIRS = [  os.path.join(BASE_DIR , 'static') ]


# Default primary key field type
# https://docs.djangoproject.com/en/4.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR , 'media')




#  settings.MEDIA_ROOT =P:\Food Delievery Web App\media
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_USE_TLS = True
EMAIL_PORT = 587
EMAIL_HOST_USER = "vikashvermacom92@gmail.com"
EMAIL_HOST_PASSWORD = "tfsyzdxzfhdhdlsd"


ACCOUNT_ADAPTER =  'restaurent.account_adapter.NoNewUserAccountAdapter'
LOGIN_REDIRECT_URL = 'dashboard'

CRISPY_TEMPLATE_PACK = 'bootstrap4'













'''
allauth',
    'allauth.account',
    'allauth.socialaccount',
    # ... include the providers you want to enable:
    'allauth.socialaccount.providers.agave',
    'allauth.socialaccount.providers.amazon',
    'allauth.socialaccount.providers.amazon_cognito',
    'allauth.socialaccount.providers.angellist',
    'allauth.socialaccount.providers.apple',
    'allauth.socialaccount.providers.asana',
    'allauth.socialaccount.providers.auth0',
    'allauth.socialaccount.providers.authentiq',
    'allauth.socialaccount.providers.azure',
    'allauth.socialaccount.providers.baidu',
    'allauth.socialaccount.providers.basecamp',
    'allauth.socialaccount.providers.battlenet',
    'allauth.socialaccount.providers.bitbucket',
    'allauth.socialaccount.providers.bitbucket_oauth2',
    'allauth.socialaccount.providers.bitly',
    'allauth.socialaccount.providers.box',
    'allauth.socialaccount.providers.cern',
    'allauth.socialaccount.providers.cilogon',
    'allauth.socialaccount.providers.clever',
    'allauth.socialaccount.providers.coinbase',
    'allauth.socialaccount.providers.dataporten',
    'allauth.socialaccount.providers.daum',
    'allauth.socialaccount.providers.digitalocean',
    'allauth.socialaccount.providers.discord',
    'allauth.socialaccount.providers.disqus',
    'allauth.socialaccount.providers.douban',
    'allauth.socialaccount.providers.doximity',
    'allauth.socialaccount.providers.draugiem',
    'allauth.socialaccount.providers.drip',
    'allauth.socialaccount.providers.dropbox',
    'allauth.socialaccount.providers.dwolla',
    'allauth.socialaccount.providers.edmodo',
    'allauth.socialaccount.providers.edx',
    'allauth.socialaccount.providers.eventbrite',
    'allauth.socialaccount.providers.eveonline',
    'allauth.socialaccount.providers.evernote',
    'allauth.socialaccount.providers.exist',
    'allauth.socialaccount.providers.facebook',
    'allauth.socialaccount.providers.feedly',
    'allauth.socialaccount.providers.figma',
    'allauth.socialaccount.providers.fivehundredpx',
    'allauth.socialaccount.providers.flickr',
    'allauth.socialaccount.providers.foursquare',
    'allauth.socialaccount.providers.frontier',
    'allauth.socialaccount.providers.fxa',
    'allauth.socialaccount.providers.gitea',
    'allauth.socialaccount.providers.github',
    'allauth.socialaccount.providers.gitlab',
    'allauth.socialaccount.providers.globus',
    'allauth.socialaccount.providers.google',
    'allauth.socialaccount.providers.gumroad',
    'allauth.socialaccount.providers.hubic',
    'allauth.socialaccount.providers.instagram',
    'allauth.socialaccount.providers.jupyterhub',
    'allauth.socialaccount.providers.kakao',
    'allauth.socialaccount.providers.keycloak',
    'allauth.socialaccount.providers.lemonldap',
    'allauth.socialaccount.providers.line',
    'allauth.socialaccount.providers.linkedin',
    'allauth.socialaccount.providers.linkedin_oauth2',
    'allauth.socialaccount.providers.mailchimp',
    'allauth.socialaccount.providers.mailru',
    'allauth.socialaccount.providers.mediawiki',
    'allauth.socialaccount.providers.meetup',
    'allauth.socialaccount.providers.microsoft',
    'allauth.socialaccount.providers.naver',
    'allauth.socialaccount.providers.nextcloud',
    'allauth.socialaccount.providers.odnoklassniki',
    'allauth.socialaccount.providers.openid',
    'allauth.socialaccount.providers.openstreetmap',
    'allauth.socialaccount.providers.orcid',
    'allauth.socialaccount.providers.patreon',
    'allauth.socialaccount.providers.paypal',
    'allauth.socialaccount.providers.persona',
    'allauth.socialaccount.providers.pinterest',
    'allauth.socialaccount.providers.pocket',
    'allauth.socialaccount.providers.quickbooks',
    'allauth.socialaccount.providers.reddit',
    'allauth.socialaccount.providers.robinhood',
    'allauth.socialaccount.providers.salesforce',
    'allauth.socialaccount.providers.sharefile',
    'allauth.socialaccount.providers.shopify',
    'allauth.socialaccount.providers.slack',
    'allauth.socialaccount.providers.snapchat',
    'allauth.socialaccount.providers.soundcloud',
    'allauth.socialaccount.providers.spotify',
    'allauth.socialaccount.providers.stackexchange',
    'allauth.socialaccount.providers.steam',
    'allauth.socialaccount.providers.stocktwits',
    'allauth.socialaccount.providers.strava',
    'allauth.socialaccount.providers.stripe',
    'allauth.socialaccount.providers.telegram',
    'allauth.socialaccount.providers.trainingpeaks',
    'allauth.socialaccount.providers.trello',
    'allauth.socialaccount.providers.tumblr',
    'allauth.socialaccount.providers.twentythreeandme',
    'allauth.socialaccount.providers.twitch',
    'allauth.socialaccount.providers.twitter',
    'allauth.socialaccount.providers.untappd',
    'allauth.socialaccount.providers.vimeo',
    'allauth.socialaccount.providers.vimeo_oauth2',
    'allauth.socialaccount.providers.vk',
    'allauth.socialaccount.providers.weibo',
    'allauth.socialaccount.providers.weixin',
    'allauth.socialaccount.providers.windowslive',
    'allauth.socialaccount.providers.xing',
    'allauth.socialaccount.providers.yahoo',
    'allauth.socialaccount.providers.yandex',
    'allauth.socialaccount.providers.ynab',
    'allauth.socialaccount.providers.zoho',
    'allauth.socialaccount.providers.zoom',
    'allauth.socialaccount.providers.okta',
    'allauth.socialaccount.providers.feishu',
    ...

'''