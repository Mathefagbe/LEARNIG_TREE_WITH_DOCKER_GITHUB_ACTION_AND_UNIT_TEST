from django.apps import AppConfig


class AccountConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'account'

    # def ready(self) -> None:
    #     from .task import add

    #     add.delay(2,3)