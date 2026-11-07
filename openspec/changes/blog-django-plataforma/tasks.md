# Tasks

## 1. Setup y configuracion del proyecto Django

- [x] 1.1 Crear estructura de proyecto Django (manage.py, settings, urls) y verificar que `python manage.py check` pasa sin errores
- [x] 1.2 Configurar settings.py: INSTALLED_APPS, DATABASES (SQLite), STATIC_URL/ROOT, MEDIA_URL/ROOT, ALLOWED_HOSTS y verificar que collectstatic recopila archivos estaticos
- [x] 1.3 Instalar dependencias (Django, pillow) en virtualenv y verificar `pip freeze` las lista

## 2. Modelos de datos y migraciones

- [x] 2.1 Crear modelo User extendido con profesion y rama de ingeniería, y verificar migracion se aplica con `python manage.py migrate`
- [x] 2.2 Crear modelo EngineeringBranch con nombre y slug unicos, y verificar migracion se aplica
- [x] 2.3 Crear modelo Article con titulo, slug, cuerpo, portada, estado, vistas, autor, rama, fechas y verificar migracion se aplica
- [x] 2.4 Crear modelo Project con titulo, descripcion, contenido, enlace, imagen, vistas, likes, autor, rama, fechas y verificar migracion se aplica
- [x] 2.5 Crear modelo Comment asociado a articulo o proyecto, autor, contenido y fecha, y verificar migracion se aplica
- [x] 2.6 Crear modelo Like para proyectos con restriccion unica (usuario, proyecto), y verificar migracion se aplica

## 3. Autenticacion y perfiles de usuario

- [x] 3.1 Implementar registro de usuario con profesion y verificar que un usuario nuevo puede crear cuenta y iniciar sesion
- [x] 3.2 Implementar login/logout y verificar redireccion correcta tras autenticacion
- [x] 3.3 Crear vista de perfil publico que muestre profesion y publicaciones del usuario, y verificar que se renderiza sin errores
- [x] 3.4 Configurar admin de Django para gestionar usuarios, ramas, articulos y proyectos, y verificar acceso al admin con superusuario

## 4. Ramas de ingeniería

- [x] 4.1 Implementar vistas de listado y detalle de ramas de ingeniería, y verificar que cada rama muestra sus articulos y proyectos
- [x] 4.2 Implementar filtrado de articulos y proyectos por rama y verificar que solo se muestra contenido de la rama seleccionada

## 5. Articulos (CRUD y vistas)

- [x] 5.1 Implementar creacion de articulos (borrador/publicado) y verificar que un usuario autenticado puede crear un articulo
- [x] 5.2 Implementar edicion y eliminacion de articulos solo por el autor, y verificar que otro usuario no puede editar/eliminar
- [x] 5.3 Implementar publicacion/despublicacion de articulos y verificar que solo articulos publicados son visibles públicamente
- [x] 5.4 Implementar conteo atomico de vistas con F() y verificar que el contador se incrementa al acceder a un articulo publicado

## 6. Proyectos (CRUD, vistas y likes)

- [x] 6.1 Implementar creacion de proyectos con enlace externo e imagen y verificar que un usuario autenticado puede crear un proyecto
- [x] 6.2 Implementar edicion y eliminacion de proyectos solo por el autor, y verificar restricciones de permiso
- [x] 6.3 Implementar conteo atomico de vistas para proyectos y verificar incremento correcto
- [x] 6.4 Implementar toggle de like en proyectos con restriccion unica por usuario y verificar que un usuario solo puede dar un like por proyecto

## 7. Comentarios

- [x] 7.1 Implementar creacion de comentarios en articulos y proyectos solo para usuarios autenticados, y verificar que se asocian correctamente
- [x] 7.2 Implementar edicion y eliminacion de comentarios solo por el autor, y verificar restricciones de permiso
- [x] 7.3 Mostrar comentarios en paginas de detalle de articulo y proyecto y verificar que se renderizan con su autor y fecha

## 8. Interfaz y templates

- [x] 8.1 Crear plantilla base con navegación (home, artículos, proyectos, ramas, perfil, login/registro) y verificar que se hereda en todas las páginas
- [x] 8.2 Implementar lista de artículos con paginación y verificar renderizado correcto
- [x] 8.3 Implementar lista de proyectos con paginación y verificar renderizado correcto
- [x] 8.4 Implementar páginas de detalle de artículo y proyecto con botones de like y comentario, y verificar interactividad básica
- [x] 8.5 Aplicar Tailwind CSS vía CDN para aspecto profesional y verificar estilos en páginas principales

## 9. Despliegue en PythonAnywhere

- [x] 9.1 Crear cuenta y web app Django en PythonAnywhere y verificar que la aplicación responde
- [x] 9.2 Configurar static y media files en el dashboard de PythonAnywhere y verificar que imágenes y CSS se sirven correctamente
- [x] 9.3 Ejecutar migrate y createsuperuser en PythonAnywhere y verificar acceso al admin
- [x] 9.4 Probar flujo completo (registro, crear artículo, crear proyecto, dar like, comentar) en el entorno desplegado

## Workflow follow-up

- Revisar todos los artifacts de planificación antes de archivar el cambio.
- Archivar el cambio una vez los requisitos de revisión del proyecto estén satisfechos.

