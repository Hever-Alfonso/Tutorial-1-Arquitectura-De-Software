from django.db import models


class Product(models.Model):
    """
    Modelo que representa un producto en la tienda en linea.
    Genera la tabla 'pages_product' en la base de datos.
    """

    # Nombre del producto, maximo 255 caracteres
    name = models.CharField(max_length=255)

    # Precio del producto en numero entero, sin decimales
    price = models.IntegerField()

    # Fecha y hora de creacion, se asigna automaticamente al crear el registro
    created_at = models.DateTimeField(auto_now_add=True)

    # Fecha y hora de ultima modificacion, se actualiza automaticamente al guardar
    updated_at = models.DateTimeField(auto_now=True)