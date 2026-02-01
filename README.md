# Tutorial 1 – Arquitectura de Software (Django)

## Descripción
Este proyecto corresponde al **Tutorial 1 de Arquitectura de Software**, desarrollado con **Django**.  
El objetivo es comprender y aplicar la arquitectura **Modelo–Vista–Template (MVT)**, creando una aplicación web básica que permite:

- Navegación entre páginas (Home, About, Products)
- Creación de productos mediante formularios
- Renderizado de vistas con templates
- Uso de estilos estáticos
- Persistencia básica con SQLite
- Gestión del proyecto usando entorno virtual (`venv`)

---

## Tecnologías usadas
- Python 3
- Django
- HTML
- CSS
- SQLite
- Git y GitHub
- Entorno virtual (`venv`)

---

## Estructura del proyecto

```
Tutorial-1-Arquitectura-De-Software/
│
├── .venv/                  # Entorno virtual (NO se sube a GitHub)
├── helloworld/
│   ├── helloworld_project/
│   │   ├── settings.py
│   │   ├── urls.py
│   │   ├── asgi.py
│   │   └── wsgi.py
│   │
│   ├── pages/
│   │   ├── migrations/
│   │   ├── static/
│   │   │   └── pages/
│   │   │       └── app.css
│   │   ├── templates/
│   │   │   ├── pages/
│   │   │   │   ├── base.html
│   │   │   │   ├── home.html
│   │   │   │   └── about.html
│   │   │   └── products/
│   │   │       ├── index.html
│   │   │       ├── create.html
│   │   │       └── show.html
│   │   ├── views.py
│   │   ├── urls.py
│   │   ├── models.py
│   │   └── apps.py
│   │
│   ├── db.sqlite3
│   └── manage.py
│
├── requirements.txt
├── README.md
└── .gitignore
```

---

## Arquitectura (MVT)

- **Modelo (Model)**  
  Definido en `models.py`. Representa la estructura de los datos.

- **Vista (View)**  
  Definida en `views.py`. Contiene la lógica que procesa las peticiones HTTP.

- **Template**  
  Archivos HTML ubicados en `templates/`. Se encargan de la presentación.

Django gestiona internamente el controlador mediante el sistema de URLs.

---

## Instalación y ejecución

### 1. Clonar el repositorio
```bash
git clone <URL_DEL_REPOSITORIO>
cd Tutorial-1-Arquitectura-De-Software
```

### 2. Crear y activar entorno virtual

**Windows (PowerShell):**
```powershell
python -m venv .venv
.venv\Scripts\activate
```

---

### 3. Instalar dependencias
```bash
pip install -r requirements.txt
```

---

### 4. Ejecutar migraciones
```bash
cd helloworld
python manage.py migrate
```

---

### 5. Ejecutar el servidor
```bash
python manage.py runserver
```

Abrir en el navegador:
```
http://127.0.0.1:8000/
```

---

## Funcionalidades implementadas
- Página Home
- Página About
- Listado de productos
- Creación de productos mediante formulario
- Validación básica de formularios
- Uso de templates base
- Estilos CSS estáticos
- Persistencia con SQLite

---

## Notas importantes
- El entorno virtual `.venv` está excluido mediante `.gitignore`
- El archivo `requirements.txt` permite replicar el entorno
- El proyecto está listo para ser extendido con nuevas funcionalidades

---

## Autor
Hever Andre Alfonso Jimenez
Universidad EAFIT
Proyecto desarrollado como parte del curso **Arquitectura de Software**.