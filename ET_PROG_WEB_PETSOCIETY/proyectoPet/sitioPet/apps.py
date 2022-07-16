from django.apps import AppConfig


class SitiopetConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'sitioPet'

class StoreConfig(AppConfig):
    name = 'store'