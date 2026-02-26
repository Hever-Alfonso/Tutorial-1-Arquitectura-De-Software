# Tutorial 3 - Arquitectura de Software (Django)

Proyecto desarrollado como parte del Taller 3 de Arquitectura de Software, utilizando el framework Django con soporte de sesiones para un carrito de compras, subida de imagenes y el Principio de Inversion de Dependencias (DIP).

El proyecto fue construido de manera incremental sobre el Tutorial 2, siguiendo estrictamente las actividades definidas en el documento guia del taller y manteniendo buenas practicas de desarrollo y control de versiones con Git.

---

## Descripcion del proyecto

La aplicacion representa una tienda en linea que persiste datos en SQLite, maneja sesiones para el carrito de compras y demuestra el Principio de Inversion de Dependencias (DIP) a traves de un sistema de subida de imagenes con y sin DI. El objetivo principal es comprender:

- El uso de sesiones en Django para persistir estado entre peticiones
- El Principio de Inversion de Dependencias (DIP) en una aplicacion real
- La diferencia practica entre una arquitectura con y sin DI
- La inyeccion de dependencias desde urls.py usando factory functions
- Clases abstractas en Python (ABC) como interfaces
- Almacenamiento de archivos con el sistema de media de Django

---

## Arquitectura aplicada (MVT + DIP)

El proyecto sigue el patron MVT (Model - View - Template) de Django e incorpora el Principio de Inversion de Dependencias:

### Model
- Modelo `Product` con campos: name, price, created_at, updated_at
- Modelo `Comment` relacionado con Product mediante ForeignKey
- Migraciones generadas automaticamente por Django

### View
- Consultas reales a la base de datos mediante el ORM de Django
- Formularios basados en ModelForm para guardar directamente en la BD
- `CartView`: usa `request.session` para almacenar el carrito entre peticiones
- `CartRemoveAllView`: elimina el carrito de la sesion actual
- `ImageViewFactory`: factory function que inyecta el storage como dependencia (DIP)
- `ImageViewNoDI`: misma funcionalidad pero con acoplamiento directo (sin DIP)

### Template
- Listado de productos desde la base de datos
- Detalle de producto con comentarios relacionados
- Formulario de creacion con confirmacion
- Pagina de carrito de compras
- Pagina de subida de imagenes (con y sin DI)

### DIP - Inversion de Dependencias
- `interfaces.py`: define `ImageStorage` como clase abstracta (el contrato)
- `utils.py`: implementa `ImageLocalStorage` que hereda de `ImageStorage`
- `apps.py`: service provider que carga la clase configurada al arrancar
- `settings.py`: `IMAGE_STORAGE_CLASS` permite cambiar la implementacion sin tocar vistas
- `urls.py`: inyecta `ImageLocalStorage()` al crear las vistas (inyeccion de dependencias)

---

## Tecnologias utilizadas

- Python 3.12
- Django 5.2
- factory-boy y Faker (generacion de datos de prueba)
- HTML (Django Templates)
- CSS
- Bootstrap
- SQLite
- Git y GitHub
- Conda (entorno virtual)
- Docker y Docker Compose

---

## Estructura del proyecto
```
.
├── helloworld/
│   ├── helloworld_project/
│   ├── media/                    # Imagenes subidas (persistidas con volumen Docker)
│   ├── pages/
│   │   ├── management/
│   │   │   └── commands/
│   │   │       └── seed_products.py
│   │   ├── migrations/
│   │   ├── static/
│   │   ├── templates/
│   │   │   ├── cart/
│   │   │   │   └── index.html
│   │   │   ├── images/
│   │   │   │   └── index.html
│   │   │   ├── imagesnotdi/
│   │   │   │   └── index.html
│   │   │   ├── pages/
│   │   │   └── products/
│   │   ├── factories.py
│   │   ├── interfaces.py         # Interfaz abstracta ImageStorage (DIP)
│   │   ├── models.py
│   │   ├── urls.py
│   │   ├── utils.py              # Implementacion concreta ImageLocalStorage
│   │   └── views.py
│   └── manage.py
├── .gitignore
├── COMMANDS.md
├── Dockerfile
├── README.md
├── docker-compose.yml
└── requirements.txt
```

---

## Funcionalidades implementadas

- Listado de productos desde la base de datos
- Detalle de producto con precio condicional (rojo si supera 2000)
- Comentarios relacionados al producto
- Creacion de productos mediante formulario con persistencia en BD
- Seeder para poblar la BD con datos de prueba
- Carrito de compras con sesiones Django (agregar y vaciar productos)
- Subida de imagenes con Inversion de Dependencias (DIP)
- Subida de imagenes sin DI (para comparacion y entendimiento del principio)

---

## Como ejecutar el proyecto

### Opcion 1: Conda

1. Clonar el repositorio
```bash
git clone <URL_DEL_REPOSITORIO>
cd DjangoTutorials
```

2. Crear y activar el entorno
```bash
conda create -n hever_tutorial_2 python=3.12
conda activate hever_tutorial_2
```

3. Instalar dependencias
```bash
pip install -r requirements.txt
```

4. Aplicar migraciones y poblar la base de datos
```bash
cd helloworld
python manage.py migrate
python manage.py seed_products
```

5. Ejecutar el servidor
```bash
python manage.py runserver
```

6. Abrir en el navegador
```
http://127.0.0.1:8000/
```

### Opcion 2: Docker
```bash
docker compose up --build
```

En una segunda terminal:
```bash
docker compose exec web python helloworld/manage.py migrate
docker compose exec web python helloworld/manage.py seed_products
```

Acceder en: http://localhost:8000

---

## Control de versiones

El proyecto utiliza Git siguiendo buenas practicas:

- Desarrollo en ramas `feat/` por actividad
- Commits con convencion Conventional Commits
- Historial limpio y trazable

Ejemplo de commit:
```
feat(pages): add ImageViewFactory with DI and ImageViewNoDI for comparison
```

---

## Autor

Hever Andre Alfonso Jimenez - Universidad EAFIT - Proyecto desarrollado como parte de un taller academico de Arquitectura de Software utilizando Django.