import environ

from .base import *  # noqa

env = environ.Env()

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = env.bool("DJANGO_DEBUG", default=False)

# SECURITY WARNING: keep the secret key used in production secret!
# Prefira sempre definir DJANGO_SECRET_KEY no ambiente (nunca versione uma
# chave real) — o valor abaixo e so o fallback gerado no momento do
# 'aratinga start', util pra rodar local sem configurar nada.
SECRET_KEY = env.str("DJANGO_SECRET_KEY", default="{{ secret_key }}")

# Add your site's domain name(s) here, ou defina DJANGO_ALLOWED_HOSTS
# (separado por virgula) no ambiente.
ALLOWED_HOSTS = env.list("DJANGO_ALLOWED_HOSTS", default=["{{ domain }}"])


# --- Banco de dados ---------------------------------------------------
# DATABASE_URL no formato sqlite:////caminho/absoluto/db.sqlite3 ou
# postgres://usuario:senha@host:porta/nome. Sem essa variavel, cai pro
# mesmo sqlite local usado em dev.
DATABASES = {
    "default": env.db(
        "DATABASE_URL", default=f"sqlite:///{BASE_DIR / 'db.sqlite3'}"  # noqa: F405
    ),
}

# O campo de busca do Wagtail usa SearchVectorField no Postgres, que exige
# 'django.contrib.postgres' em INSTALLED_APPS (nao precisa disso no
# sqlite) — sem isso o "manage.py check" falha com postgres.E005.
INSTALLED_APPS = list(INSTALLED_APPS)  # noqa: F405
if DATABASES["default"]["ENGINE"] == "django.db.backends.postgresql":
    INSTALLED_APPS.append("django.contrib.postgres")


# --- Arquivos estaticos --------------------------------------------
# Whitenoise serve os estaticos direto do processo do gunicorn, com
# cache-busting via manifest — dispensa um servidor/imagem nginx separada
# so pra isso. Precisa rodar 'collectstatic' antes do primeiro start.
MIDDLEWARE = list(MIDDLEWARE)  # noqa: F405
MIDDLEWARE.insert(
    MIDDLEWARE.index("django.middleware.security.SecurityMiddleware") + 1,
    "whitenoise.middleware.WhiteNoiseMiddleware",
)

STORAGES = {
    "default": {
        "BACKEND": "django.core.files.storage.FileSystemStorage",
    },
    "staticfiles": {
        "BACKEND": "whitenoise.storage.CompressedManifestStaticFilesStorage",
    },
}


# --- Cache / sessao ----------------------------------------------------
# Redis se REDIS_URL estiver definida (redis://host:porta/db); sem ela,
# cai pro cache em arquivo local (comportamento original deste template —
# ok pra um site pequeno/single-container, nao escala em varias replicas).
REDIS_URL = env.str("REDIS_URL", default="")
if REDIS_URL:
    CACHES = {
        "default": {
            "BACKEND": "django.core.cache.backends.redis.RedisCache",
            "LOCATION": REDIS_URL,
            "KEY_PREFIX": "aratinga",
            "TIMEOUT": 14400,  # in seconds
        }
    }
    SESSION_ENGINE = "django.contrib.sessions.backends.cache"
    SESSION_CACHE_ALIAS = "default"
else:
    CACHES = {
        "default": {
            "BACKEND": "django.core.cache.backends.filebased.FileBasedCache",
            "LOCATION": BASE_DIR / "cache",  # noqa: F405
            "KEY_PREFIX": "aratinga",
            "TIMEOUT": 14400,  # in seconds
        }
    }


# --- Proxy reverso / TLS -----------------------------------------------
# Ative DJANGO_SSL_PROXY=true somente se houver um proxy reverso confiavel
# na frente (Traefik, Cloudflare, nginx do host, etc.) fazendo terminacao
# TLS e repassando X-Forwarded-Proto; caso contrario deixe desligado.
if env.bool("DJANGO_SSL_PROXY", default=False):
    SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "https")
    SESSION_COOKIE_SECURE = True
    CSRF_COOKIE_SECURE = True
    SECURE_SSL_REDIRECT = True
    SECURE_HSTS_SECONDS = env.int("DJANGO_HSTS_SECONDS", default=31536000)

CSRF_TRUSTED_ORIGINS = env.list("DJANGO_CSRF_TRUSTED_ORIGINS", default=[])


# --- Email -----------------------------------------------------------
# To send email from the server, we recommend django_sendmail_backend
# Or specify your own email backend such as an SMTP server.
# https://docs.djangoproject.com/en/{{ docs_version }}/ref/settings/#email-backend
# EMAIL_BACKEND = "django_sendmail_backend.backends.EmailBackend"

# Default email address used to send messages from the website.
DEFAULT_FROM_EMAIL = env.str(
    "DJANGO_DEFAULT_FROM_EMAIL",
    default="{{ sitename }} <info@{{ domain_nowww }}>",
)

# A list of people who get error notifications.
ADMINS = [
    (
        "Administrator",
        env.str("DJANGO_ADMIN_EMAIL", default="admin@{{ domain_nowww }}"),
    ),
]

# A list in the same format as ADMINS that specifies who should get broken link
# (404) notifications when BrokenLinkEmailsMiddleware is enabled.
MANAGERS = ADMINS

# Email address used to send error messages to ADMINS.
SERVER_EMAIL = DEFAULT_FROM_EMAIL


# --- Wagtail admin -----------------------------------------------------
# Base URL to use when referring to full URLs within the Wagtail admin backend -
# e.g. in notification emails. Don't include '/admin' or a trailing slash
WAGTAILADMIN_BASE_URL = env.str(
    "WAGTAILADMIN_BASE_URL", default="http://{{ domain }}"
)
