from django.urls import path

# Importamos todas las vistas necesarias incluyendo ProductCreatedView
# que es la vista de confirmacion despues de crear un producto,
# y las vistas del carrito que usan sesiones de Django
from .views import (
    HomePageView,
    AboutPageView,
    ContactPageView,
    ProductIndexView,
    ProductShowView,
    ProductCreateView,
    ProductCreatedView,
    CartView,
    CartRemoveAllView,
)

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('about/', AboutPageView.as_view(), name='about'),
    path('contact/', ContactPageView.as_view(), name='contact'),
    path('products/', ProductIndexView.as_view(), name='index'),
    path('products/create', ProductCreateView.as_view(), name='form'),
    # Ruta de confirmacion: se activa despues de guardar un producto exitosamente
    path('products/create/success', ProductCreatedView.as_view(), name='product-created'),
    path('products/<str:id>', ProductShowView.as_view(), name='show'),
    # Rutas del carrito de compras (usan sesiones para persistencia)
    path('cart/', CartView.as_view(), name='cart_index'),
    path('cart/add/<str:product_id>', CartView.as_view(), name='cart_add'),
    path('cart/removeAll', CartRemoveAllView.as_view(), name='cart_removeAll'),
]