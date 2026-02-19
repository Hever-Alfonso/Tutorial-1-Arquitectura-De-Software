from django.urls import path

# Importamos todas las vistas necesarias incluyendo ProductCreatedView
# que es la vista de confirmacion despues de crear un producto
from .views import HomePageView, AboutPageView, ContactPageView, ProductIndexView, ProductShowView, ProductCreateView, ProductCreatedView

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('about/', AboutPageView.as_view(), name='about'),
    path('contact/', ContactPageView.as_view(), name='contact'),
    path('products/', ProductIndexView.as_view(), name='index'),
    path('products/create', ProductCreateView.as_view(), name='form'),
    # Ruta de confirmacion: se activa despues de guardar un producto exitosamente
    path('products/create/success', ProductCreatedView.as_view(), name='product-created'),
    path('products/<str:id>', ProductShowView.as_view(), name='show'),
]