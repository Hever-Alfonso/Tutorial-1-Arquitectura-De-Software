# Tutorial 1 – Arquitectura de Software (Django)

Proyecto desarrollado como parte del Taller 1 de Arquitectura de Software, utilizando el framework Django y aplicando el patrón arquitectónico MVT (Model – View – Template).

El proyecto fue construido de manera incremental, siguiendo estrictamente las actividades definidas en el documento guía del taller y manteniendo buenas prácticas de desarrollo y control de versiones con Git.

---

## Descripción del proyecto

La aplicación representa una tienda en línea básica, cuyo objetivo principal es comprender:

- La estructura de un proyecto Django
- El manejo de vistas, templates y rutas
- El uso de formularios y validaciones
- El flujo completo de una aplicación web
- El control de versiones con Git y GitHub

Este proyecto no persiste productos en base de datos, ya que el enfoque del taller es arquitectónico y no de persistencia.

---

## Arquitectura aplicada (MVT)

El proyecto sigue el patrón MVT (Model – View – Template) de Django:

### Model
- Representado por estructuras simples (listas y diccionarios)
- Simula los datos de productos

### View
- Maneja la lógica de negocio
- Procesa peticiones HTTP
- Valida datos
- Controla el flujo de la aplicación

### Template
- Encargado únicamente de la presentación
- Usa herencia de templates
- Implementa condicionales y variables de contexto

---

## Tecnologías utilizadas

- Python 3
- Django
- HTML (Django Templates)
- CSS
- Bootstrap
- SQLite (configuración por defecto de Django)
- Git y GitHub
- Entorno virtual (venv)

---

## Estructura del proyecto

```
.
├── .venv/
├── helloworld/
│   ├── helloworld_project/
│   ├── pages/
│   │   ├── __pycache__/
│   │   ├── migrations/
│   │   ├── static/
│   │   │   └── pages/
│   │   │       └── app.css
│   │   ├── templates/
│   │   │   ├── pages/
│   │   │   │   ├── base.html
│   │   │   │   ├── home.html
│   │   │   │   ├── about.html
│   │   │   │   └── contact.html
│   │   │   └── products/
│   │   │       ├── index.html
│   │   │       ├── show.html
│   │   │       ├── create.html
│   │   │       └── created.html
│   │   ├── __init__.py
│   │   ├── admin.py
│   │   ├── apps.py
│   │   ├── models.py
│   │   ├── tests.py
│   │   ├── urls.py
│   │   └── views.py
│   ├── db.sqlite3
│   └── manage.py
├── .gitignore
├── README.md
└── requirements.txt
```

---

## Funcionalidades implementadas

- Página Home
- Página About
- Página Contact
- Listado de productos
- Detalle de productos
- Creación de productos mediante formulario
- Validaciones de formulario
- Confirmación de creación de producto
- Navegación completa desde el menú

---

## Cómo ejecutar el proyecto

### 1. Clonar el repositorio
```
git clone <URL_DEL_REPOSITORIO>
cd tutorial-1-arquitectura
```

### 2. Crear y activar el entorno virtual

Linux / macOS:
```
python3 -m venv .venv
source .venv/bin/activate
```

Windows:
```
python -m venv .venv
.venv\Scripts\activate
```

### 3. Instalar dependencias
```
pip install -r requirements.txt
```

### 4. Ejecutar el servidor
```
cd helloworld
python manage.py runserver
```

### 5. Abrir en el navegador
```
http://127.0.0.1:8000/
```

---

## Control de versiones

El proyecto utiliza Git siguiendo buenas prácticas:

- Desarrollo por ramas (una por cada activity)
- Commits con convención Conventional Commits
- Historial limpio y trazable
- Las ramas de actividades se conservan como evidencia del proceso

Ejemplo de commit:
```
feat(products): add product created confirmation page
```

---

## Estado del proyecto

- Todas las actividades del taller han sido completadas
- El proyecto funciona correctamente
- La arquitectura MVT está correctamente aplicada
- El repositorio contiene el historial completo del desarrollo

---

## Autor

Hever Andre Alfonso Jimenez - Universidad EAFIT - Proyecto desarrollado como parte de un taller académico de Arquitectura de Software utilizando Django.