from django.apps import AppConfig
from django.apps import apps
from django.core.exceptions import ImproperlyConfigured


class DjangoHtmxRefreshConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'django_htmx_refresh'
    def ready(self):
        if not apps.is_installed('django_htmx'):
            raise ImproperlyConfigured("'django_htmx_refresh' requires you to have the 'django_htmx' application installed. Try using 'pip install django-htmx' or checking your INSTALLED_APPS setting. ")
