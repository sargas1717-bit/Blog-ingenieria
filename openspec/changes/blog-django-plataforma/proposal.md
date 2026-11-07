# Proposal

## Why

Un ingeniero necesita un lugar profesional para publicar artículos técnicos y proyectos de investigación o trabajo, organizados por rama de ingeniería, con interacción de la comunidad (comentarios, likes, conteo de vistas). No existe hoy una plataforma propia que unifique publicación, perfil de ingeniero con profesión, y métricas de engagement bajo un stack Django desplegable en PythonAnywhere (plan gratuito).

## What Changes

- Nueva aplicación Django con stack completo (modelos, vistas, templates, URLs, admin).
- Modelo de usuario extendido con profesión y rama de ingeniería.
- CRUD de artículos: crear, editar, eliminar, publicar/desechar, contar vistas.
- CRUD de proyectos: crear, editar, eliminar, enlace GitHub/demo, contar vistas y likes.
- Catálogo de ramas de ingeniería para agrupar artículos y proyectos.
- Comentarios en artículos y proyectos (usuario autenticado).
- Likes en proyectos (toggle, usuario autenticado).
- Perfil público de ingeniero con sus publicaciones.
- Admin de Django para gestión de usuarios, ramas, artículos y proyectos.
- Despliegue en PythonAnywhere (plan gratuito): SQLite, static/media, WSGI.

## Capabilities

### New Capabilities

- user-auth: registro, login, logout, perfiles de usuario con profesión, admin de usuarios.
- articles: CRUD de artículos, estados borrador/publicado, conteo de vistas, detalle público.
- projects: CRUD de proyectos, enlaces externos, conteo de vistas y likes, detalle público.
- engineering-branches: catálogo de ramas de ingeniería, agrupación de artículos y proyectos por rama.
- comments: comentarios en artículos y proyectos, solo usuarios autenticados.
- interactions: likes en proyectos, conteo atómico de vistas.

### Modified Capabilities

- (none)

## Impact

- Reemplaza el scaffold Next.js actual por Django como stack principal.
- Nueva base de datos SQLite en /home/adakademy/Documents/blog_open_spec.
- Nuevas dependencias Python: Django, pillow (opcional para imágenes).
- Despliegue en PythonAnywhere con configuración de static/media y WSGI.
- No se afectan servicios externos existentes.
