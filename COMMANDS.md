# Proyecto Django Dockerizado (Modo Demo Sencillo)

Este documento describe los comandos necesarios para ejecutar y manejar el proyecto usando Docker y Docker Compose.

El objetivo es que el proyecto funcione con el menor número de pasos posible, pero manteniendo persistencia de datos y control básico del contenedor.

## Conceptos clave

- Imagen: plantilla construida a partir del Dockerfile.
- Contenedor: instancia en ejecución de una imagen.
- Contenedores son efímeros: si se recrean, su sistema de archivos interno se pierde.
- Volúmenes: almacenamiento persistente fuera del contenedor.
- En este proyecto, el volumen guarda la base de datos SQLite.

## Levantar el proyecto (comando principal)

```bash
docker compose up --build
```

Este comando construye e inicia los contenedores definidos en `docker-compose.yml`.

Una vez el contenedor esté corriendo, verás en la terminal un mensaje como:

```
web-1 | Starting development server at http://0.0.0.0:8000/
```

Esto significa que puedes abrir el navegador y acceder a la aplicación desde:

```
http://localhost:8000
```

Con esto, el servidor Django estará activo dentro del contenedor y listo para usarse.