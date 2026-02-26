from django.apps import AppConfig
from django.utils.module_loading import import_string
from django.conf import settings


class PagesConfig(AppConfig):
    """
    Configuracion de la aplicacion 'pages'.

    El metodo ready() actua como service provider:
    al arrancar Django, importa la clase de storage configurada
    en settings.IMAGE_STORAGE_CLASS. Esto valida que la clase
    existe y esta correctamente configurada antes de recibir requests.

    Esto es parte del patron DIP: la aplicacion sabe que hay un
    ImageStorage, pero no cual implementacion concreta se usara
    hasta leer la configuracion.
    """

    default_auto_field = 'django.db.models.BigAutoField'
    name = 'pages'

    def ready(self):
        # Carga la clase de storage al inicio de la aplicacion
        # Si IMAGE_STORAGE_CLASS apunta a una clase inexistente, falla rapido
        import_string(settings.IMAGE_STORAGE_CLASS)