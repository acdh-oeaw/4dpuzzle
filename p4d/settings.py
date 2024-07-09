import os
from pathlib import Path


os.environ["DJANGO_ALLOW_ASYNC_UNSAFE"] = "true"

SHARED_URL = "https://shared.acdh.oeaw.ac.at/"
PROJECT_NAME = "p4d"
DEFAULT_AUTO_FIELD = "django.db.models.AutoField"

BASE_DIR = Path(__file__).resolve().parent.parent

REDMINE_ID = os.environ.get("REDMINE_ID", "7601")
ACDH_IMPRINT_URL = "https://imprint.acdh.oeaw.ac.at/"
SECRET_KEY = os.environ.get("SECRET_KEY", "rlYWFQbFuwofjjafjwo")


if os.environ.get("DEBUG", False):
    DEBUG = True
else:
    DEBUG = False

ADD_ALLOWED_HOST = os.environ.get("ALLOWED_HOST", "*")
ALLOWED_HOSTS = [
    "127.0.0.1",
    "0.0.0.0",
    ADD_ALLOWED_HOST,
]

INSTALLED_APPS = [
    "dal",
    "django.contrib.admin",
    "dal_select2",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "mptt",
    "django_extensions",
    "crispy_forms",
    "crispy_bootstrap3",
    "django_filters",
    "django_tables2",
    "rest_framework",
    "idprovider",
    "webpage",
    "browsing",
    "vocabs",
    "infos",
    "archiv",
    "archeutils",
    "netvis",
    "charts",
    "filechecker",
    "qgisapp",
]

CRISPY_ALLOWED_TEMPLATE_PACKS = "bootstrap3"
CRISPY_TEMPLATE_PACK = "bootstrap3"

REST_FRAMEWORK = {
    "DEFAULT_PERMISSION_CLASSES": (
        "rest_framework.permissions.IsAuthenticatedOrReadOnly",
    ),
}

REST_FRAMEWORK = {
    "DEFAULT_PERMISSION_CLASSES": (
        "rest_framework.permissions.IsAuthenticatedOrReadOnly",
    )
}

SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "https")

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "p4d.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
                "webpage.webpage_content_processors.installed_apps",
                "webpage.webpage_content_processors.is_dev_version",
                "webpage.webpage_content_processors.get_db_name",
                "webpage.webpage_content_processors.shared_url",
                "webpage.webpage_content_processors.my_app_name",
            ],
        },
    },
]

WSGI_APPLICATION = "p4d.wsgi.application"

if os.environ.get("POSTGRES_DB"):
    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.postgresql",
            "NAME": os.environ.get("POSTGRES_DB", "p4d"),
            "USER": os.environ.get("POSTGRES_USER", "postgres"),
            "PASSWORD": os.environ.get("POSTGRES_PASSWORD", "postgres"),
            "HOST": os.environ.get("POSTGRES_HOST", "localhost"),
            "PORT": os.environ.get("POSTEGRES_PORT", "5432"),
        }
    }
else:
    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.sqlite3",
            "NAME": BASE_DIR / "db.sqlite3",
        }
    }


AUTHENTICATION_BACKENDS = ("django.contrib.auth.backends.ModelBackend",)

# Password validation
# https://docs.djangoproject.com/en/1.11/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]


# Internationalization
# https://docs.djangoproject.com/en/1.11/topics/i18n/

LANGUAGE_CODE = "en"

TIME_ZONE = "UTC"

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.11/howto/static-files/

STATIC_ROOT = os.path.join(BASE_DIR, "staticfiles/")
STATIC_URL = "/static/"
MEDIA_ROOT = os.path.join(BASE_DIR, "media/")
MEDIA_URL = "/media/"
VOCABS_DEFAULT_PEFIX = os.path.basename(BASE_DIR)
VOCABS_SETTINGS = {
    "default_prefix": VOCABS_DEFAULT_PEFIX,
    "default_ns": "http://www.vocabs/{}/".format(VOCABS_DEFAULT_PEFIX),
    "default_lang": "en",
}
ARCHE_BASE_URI = "https://id.acdh.oeaw.ac.at/td-archiv"
ARCHE_LANG = "en"
ARCHE_PREFIX_REMOVE = r"R:/OREA-EGYPT_Puzzle4D/ARCHE-preparation/original/"
ARCHE_CONST_MAPPINGS = [
    # ('hasOwner', "https://id.acdh.oeaw.ac.at/OREA",),
    # ('hasOwner', "https://id.acdh.oeaw.ac.at/OAI",),
    # ('hasContact', "https://id.acdh.oeaw.ac.at/OREA",),
    # ('hasContact', "https://id.acdh.oeaw.ac.at/OAI",),
    # ('hasRightsHolder', "https://id.acdh.oeaw.ac.at/OREA",),
    # ('hasRightsHolder', "https://id.acdh.oeaw.ac.at/OAI",),
    # ('hasLicensor', 'https://id.acdh.oeaw.ac.at/OREA',),
    # ('hasLicensor', 'https://id.acdh.oeaw.ac.at/OAI',),
    # ('hasLicense', 'https://vocabs.acdh.oeaw.ac.at/license/cc-by-40',),
    # ('hasRelatedDiscipline', 'https://vocabs.acdh.oeaw.ac.at/oefosdisciplines/601003',),
    # ('hasMetadataCreator', 'https://id.acdh.oeaw.ac.at/OAI',),
    # ('hasDepositor', 'https://id.acdh.oeaw.ac.at/OAI',),
    # ('hasAvailableDate', '2020-02-01',),
    # ('hasPrincipalInvestigator', 'https://id.acdh.oeaw.ac.at/bhorejs',),
]
FC_DEFAULT_ACCESS_RES = (
    "https://vocabs.acdh.oeaw.ac.at/archeaccessrestrictions/restricted"
)
FC_DEFAULT_ACCESS_COL = "https://vocabs.acdh.oeaw.ac.at/archeaccessrestrictions/public"
