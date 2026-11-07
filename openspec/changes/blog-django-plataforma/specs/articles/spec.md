# Spec Delta

## Purpose

Gestiona la publicación y lectura de artículos técnicos, incluyendo estados de publicación y conteo de vistas.

## ADDED Requirements

### Requirement: Author can create an article
El sistema SHALL permitir a un usuario autenticado crear un artículo con título, cuerpo, slug, imagen de portada y estado de publicación.

#### Scenario: Successful article creation
- **WHEN** un usuario autenticado envía el formulario de creación con datos válidos
- **THEN** el sistema crea el artículo en estado borrador y asigna al autor actual

#### Scenario: Slug auto-generated from title
- **WHEN** un usuario crea un artículo sin slug explícito
- **THEN** el sistema genera el slug a partir del título

### Requirement: Article can be published or unpublished
El sistema SHALL permitir al autor o a un administrador cambiar el estado de publicado de un artículo.

#### Scenario: Publish article
- **WHEN** el autor marca un artículo como publicado
- **THEN** el artículo es visible públicamente y su fecha de publicación se registra

#### Scenario: Unpublish article
- **WHEN** el autor despublica un artículo
- **THEN** el artículo deja de ser visible públicamente

### Requirement: Any user can read published articles
El sistema SHALL permitir a cualquier usuario (autenticado o no) leer artículos publicados.

#### Scenario: Read published article
- **WHEN** un usuario solicita un artículo publicado por su slug
- **THEN** el sistema muestra el artículo completo

#### Scenario: Unpublished article not visible
- **WHEN** un usuario solicita un artículo no publicado
- **THEN** el sistema devuelve un error 404 a no ser que el usuario sea el autor o administrador

### Requirement: Author can edit or delete their own article
El sistema SHALL permitir al autor de un artículo editarlo o eliminarlo.

#### Scenario: Author edits own article
- **WHEN** el autor de un artículo envía cambios válidos
- **THEN** el sistema actualiza el artículo y conserva el autor original

#### Scenario: Author deletes own article
- **WHEN** el autor elimina su propio artículo
- **THEN** el sistema elimina el artículo y sus comentarios asociados

#### Scenario: Other user cannot edit article
- **WHEN** un usuario que no es el autor intenta editar un artículo
- **THEN** el sistema rechaza la acción con un error de permiso

### Requirement: Article views are counted
El sistema SHALL incrementar el contador de vistas cada vez que se accede a un artículo publicado.

#### Scenario: View counter incremented
- **WHEN** un usuario accede a un artículo publicado
- **THEN** el sistema incrementa el contador de vistas del artículo en uno

