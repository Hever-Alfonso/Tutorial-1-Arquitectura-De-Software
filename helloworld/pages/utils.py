from django.core.files.storage import default_storage
from django.http import HttpRequest

from .interfaces import ImageStorage


class ImageLocalStorage(ImageStorage):
    """
    Implementacion concreta de ImageStorage que guarda imagenes
    en el sistema de archivos local del servidor.

    Hereda de ImageStorage (la interfaz abstracta) e implementa
    el metodo store() usando el sistema de archivos de Django.

    Si en el futuro se quisiera cambiar a S3 o Google Cloud,
    solo se crearia una nueva clase que implemente ImageStorage
    sin tocar las vistas.
    """

    def store(self, request: HttpRequest):
        """
        Recibe el request, extrae el archivo 'profile_image',
        lo guarda en la carpeta uploaded_images/ y retorna su URL.
        Retorna None si no se envio ningun archivo.
        """
        profile_image = request.FILES.get('profile_image', None)
        if profile_image:
            # Guarda el archivo en media/uploaded_images/ usando el storage de Django
            file_name = default_storage.save(
                'uploaded_images/' + profile_image.name,
                profile_image
            )
            # Retorna la URL publica del archivo guardado
            return default_storage.url(file_name)
        return None