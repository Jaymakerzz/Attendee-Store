import certifi
import os
import dj_database_url
from .common import *

DEBUG = False
SECRET_KEY = os.environ["SECRET_KEY"]


def env_list(name):
    return [v.strip() for v in os.environ.get(name, "").split(",") if v.strip()]


ALLOWED_HOSTS = env_list("ALLOWED_HOSTS")
CSRF_TRUSTED_ORIGINS = env_list("CSRF_TRUSTED_ORIGINS")
SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "https")


DATABASES = {
    "default": dj_database_url.config(
        env="DATABASE_URL", conn_max_age=600, conn_health_checks=True
    )
}
DATABASES["default"].setdefault("OPTIONS", {})["ssl"] = {"ca": certifi.where()}


AWS_ACCESS_KEY_ID = os.environ["STORAGE_KEY_ID"]
AWS_SECRET_ACCESS_KEY = os.environ["STORAGE_SECRET"]
AWS_STORAGE_BUCKET_NAME = os.environ["STORAGE_BUCKET"]
# https://<ACCOUNT_ID>.r2.cloudflarestorage.com
AWS_S3_ENDPOINT_URL = os.environ["STORAGE_ENDPOINT"]
AWS_S3_REGION_NAME = "auto"
AWS_S3_SIGNATURE_VERSION = "s3v4"
# pub-xxxx.r2.dev or media.yourdomain.com (no https://)
AWS_S3_CUSTOM_DOMAIN = os.environ["MEDIA_DOMAIN"]
AWS_S3_FILE_OVERWRITE = False
AWS_QUERYSTRING_AUTH = False
AWS_DEFAULT_ACL = None   # R2 doesn't support ACLs, so none should be sent

STORAGES = {
    "default": {"BACKEND": "storages.backends.s3.S3Storage"},
    "staticfiles": {"BACKEND": "whitenoise.storage.CompressedManifestStaticFilesStorage"},
}

SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True
SECURE_SSL_REDIRECT = os.environ.get("SECURE_SSL_REDIRECT", "False") == "True"
SECURE_HSTS_SECONDS = int(os.environ.get("SECURE_HSTS_SECONDS", "0"))
