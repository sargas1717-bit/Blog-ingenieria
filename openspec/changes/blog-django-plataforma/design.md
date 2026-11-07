# Design

## Context

El proyecto es un scaffold Next.js 16 vacio con una raiz OpenSpec inicializada pero sin specs ni codigo de aplicacion. El cambio reemplaza el stack frontend por Django como plataforma principal, desplegada en PythonAnywhere (plan gratuito) con SQLite como base de datos. No hay base de datos existente, ni autenticacion, ni modelos de contenido.

## Goals / Non-Goals

**Goals:**
- Plataforma Django completa con CRUD de articulos y proyectos
- Autenticacion de usuarios con perfiles y profesion
- Comentarios y likes en contenido publicado
- Conteo atomico de vistas
- Despliegue en PythonAnywhere gratuito (SQLite, static/media, WSGI)
- Interfaz profesional con Django templates + Tailwind CSS via CDN

**Non-Goals:**
- API REST separada para frontend externo (Django templates sirven el HTML)
- Tareas en segundo plano con Celery (no disponible en plan gratuito)
- Base de datos MySQL/PostgreSQL (plan gratuito de PythonAnywhere usa SQLite)
- Multi-tenancy o varios sitios en una sola instancia

## Decisions

### Django sobre Next.js
**Decisión:** Usar Django como stack unico, dejando el scaffold Next.js de lado.
**Razón:** PythonAnywhere despliega aplicaciones Python de forma nativa; Next.js requiere configuracion adicional de servidor Node que no esta soportada en el plan gratuito. Django incluye admin, auth, ORM y templates todo en uno.
**Alternativa considerada:** Mantener Next.js + Django como API separada. Rechazada por complejidad de despliegue en PythonAnywhere gratis.

### Django templates + Tailwind CDN
**Decisión:** Renderizar HTML con Django templates y aplicar estilos con Tailwind CSS via CDN.
**Razón:** Evita un paso de build y sirve HTML directamente desde Django, simplificando el despliegue en PythonAnywhere.
**Alternativa considerada:** React/Vue consumiendo API de Django. Rechazada por requerir build step y despliegue de frontend separado.

### SQLite en PythonAnywhere
**Decisión:** Usar SQLite como base de datos en el plan gratuito.
**Razón:** PythonAnywhere gratis solo soporta SQLite sin coste adicional. Es suficiente para un prototipo con un solo web app.
**Riesgo:** Escrituras concurrentes (vistas, likes) pueden contender. Mitigado con F() para updates atomicos.

### Actualización atomica de vistas y likes
**Decisión:** Usar F() de Django para todos los contadores.
**Razón:** Evita condiciones de carrera en SQLite cuando múltiples requests incrementan el mismo contador simultáneamente.

### Capacidades separadas en specs
**Decisión:** Seis capacidades independientes: user-auth, articles, projects, engineering-branches, comments, interactions.
**Razón:** Cada una cubre un comportamiento del sistema que puede evolucionar por separado. No se usa un catch-all generico.

## Risks / Trade-offs

| Riesgo | Mitigación |
|--------|------------|
| Escrituras concurrentes en SQLite (vistas, likes) | F() para updates atomicos, transacciones cortas |
| Imagenes y archivos media en PythonAnywhere | Configurar MEDIA_ROOT y mapear /media/ en el dashboard web de PA |
| Plan gratuito suspende la web app tras inactividad | La web app se reactiva al visitarla; aceptable para prototipo |
| Sin Celery para emails/notificaciones | Usar Django signals sincronos o diferir a una fase posterior |
| Spam en comentarios | Moderacion por admin y posibilidad de CAPTCHA futuro |

## Migration Plan

1. Crear cuenta en PythonAnywhere y web app (Django)
2. Subir codigo del proyecto (git o manual)
3. Crear virtualenv e instalar dependencias (Django, pillow)
4. Configurar settings.py: STATIC_URL, STATIC_ROOT, MEDIA_URL, MEDIA_ROOT, ALLOWED_HOSTS
5. En dashboard de PythonAnywhere: Web -> Static files (mapear /static/ y /media/)
6. Ejecutar python manage.py collectstatic, migrate, createsuperuser
7. Configurar WSGI file para apuntar al application de Django
8. Probar en la URL asignada por PythonAnywhere

**Rollback:** Desactivar la web app en PythonAnywhere y restaurar la version anterior del codigo.

## Open Questions

- ¿Se requiere almacenamiento externo para imagenes (S3, Cloudinary) o MEDIA_ROOT local es suficiente?
- ¿Se necesita validacion de email en el registro (verificacion por correo) o solo registro inmediato?

