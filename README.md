# Tutorial 3 - Arquitectura de Software (Django)

Proyecto desarrollado como parte del Taller 3 de Arquitectura de Software, utilizando el framework Django con soporte de sesiones para un carrito de compras, y dependencias entre modelos.

El proyecto fue construido de manera incremental sobre el Tutorial 2, siguiendo estrictamente las actividades definidas en el documento guia del taller y manteniendo buenas practicas de desarrollo y control de versiones con Git.

---

## Descripcion del proyecto

La aplicacion representa una tienda en linea que ya persiste datos realmente en una base de datos SQLite, e incorpora un sistema de carrito de compras usando sesiones de Django. El objetivo principal es comprender:

- El uso de sesiones en Django para persistir estado entre peticiones
- Vistas que manejan GET y POST de forma distinta (carrito)
- La creacion y uso de modelos Django con relaciones
- El sistema de migraciones
- El uso de factories y seeders para datos de prueba
- El ORM de Django para consultar la base de datos
- El flujo completo de una aplicacion web con persistencia real

---

## Arquitectura aplicada (MVT)

El proyecto sigue el patron MVT (Model - View - Template) de Django:

### Model
- Modelo `Product` con campos: name, price, created_at, updated_at
- Modelo `Comment` relacionado con Product mediante ForeignKey
- Migraciones generadas automaticamente por Django

### View
- Consultas reales a la base de datos mediante el ORM de Django
- Formularios basados en ModelForm para guardar directamente en la BD
- Vistas genericas de Django (ListView)
- `CartView`: usa `request.session` para almacenar el carrito entre peticiones
- `CartRemoveAllView`: elimina el carrito de la sesion actual

### Template
- Listado de productos desde la base de datos
- Detalle de producto con comentarios relacionados
- Formulario de creacion con confirmacion
- Pagina de carrito de compras con productos disponibles y productos agregados

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

---

## Estructura del proyecto
```
.
├── helloworld/
│   ├── helloworld_project/
│   ├── pages/
│   │   ├── management/
│   │   │   └── commands/
│   │   │       └── seed_products.py
│   │   ├── migrations/
│   │   ├── static/
│   │   ├── templates/
│   │   │   ├── cart/
│   │   │   │   └── index.html
│   │   │   ├── pages/
│   │   │   └── products/
│   │   ├── factories.py
│   │   ├── models.py
│   │   ├── urls.py
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
- Confirmacion de creacion
- Seeder para poblar la BD con datos de prueba
- Migraciones de base de datos
- Carrito de compras con sesiones Django (agregar y vaciar productos)

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

Acceder en: http://localhost:8000

---

## Control de versiones

El proyecto utiliza Git siguiendo buenas practicas:

- Desarrollo en ramas `feat/` por actividad
- Commits con convencion Conventional Commits
- Historial limpio y trazable

Ejemplo de commit:
```
feat(pages): add CartView and CartRemoveAllView with session support
```

---

## Autor

Hever Andre Alfonso Jimenez - Universidad EAFIT - Proyecto desarrollado como parte de un taller academico de Arquitectura de Software utilizando Django.