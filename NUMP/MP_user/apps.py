from django.apps import AppConfig


class MpUserConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'MP_user'

    def ready(self):
        import MP_user.signals
