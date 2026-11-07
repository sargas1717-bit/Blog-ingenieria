# Spec Delta

## Purpose

Permite a usuarios autenticados comentar en artículos y proyectos, fomentando la interacción de la comunidad.

## ADDED Requirements

### Requirement: Authenticated user can comment on an article
El sistema SHALL permitir a un usuario autenticado escribir un comentario en un artículo publicado.

#### Scenario: Comment on article
- **WHEN** un usuario autenticado envía un comentario en un artículo
- **THEN** el sistema crea el comentario asociado al artículo y al usuario

### Requirement: Authenticated user can comment on a project
El sistema SHALL permitir a un usuario autenticado escribir un comentario en un proyecto publicado.

#### Scenario: Comment on project
- **WHEN** un usuario autenticado envía un comentario en un proyecto
- **THEN** el sistema crea el comentario asociado al proyecto y al usuario

### Requirement: Comment author can edit or delete their comment
El sistema SHALL permitir al autor de un comentario editarlo o eliminarlo.

#### Scenario: Edit own comment
- **WHEN** el autor de un comentario envía cambios válidos
- **THEN** el sistema actualiza el comentario

#### Scenario: Delete own comment
- **WHEN** el autor elimina su propio comentario
- **THEN** el sistema elimina el comentario

#### Scenario: Other user cannot edit comment
- **WHEN** un usuario que no es el autor intenta editar un comentario
- **THEN** el sistema rechaza la acción con un error de permiso

