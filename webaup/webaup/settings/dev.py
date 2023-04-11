from .base import *  # noqa: F403, F401

DEBUG = True

# WAGTAILADMIN_BASE_URL required for notification emails
WAGTAILADMIN_BASE_URL = "http://localhost:8000"

ALLOWED_HOSTS = ["*"]

EMAIL_BACKEND ="django.core.mail.backends.smtp.EmailBackend"
EMAIL_HOST = "smtp.gmail.com"
EMAIL_USE_TLS = True
EMAIL_PORT = 587
EMAIL_HOST_USER = "pythonlip@gmail.com"
EMAIL_HOST_PASSWORD = "xnmcjhagcksosciq"
EMAIL_USE_TLS = True
EMAIL_FAIL_SILENT = False 
