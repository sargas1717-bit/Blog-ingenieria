# Spec Delta

## Purpose

Gestiona la publicación y descubrimiento de proyectos de ingeniería, con likes y conteo de vistas.

## ADDED Requirements

### Requirement: Author can create a project
El sistema SHALL permitir a un usuario autenticado crear un proyecto con título, descripción, contenido, enlace externo, imagen y rama de ingeniería.

#### Scenario: Successful project creation
- **WHEN** un usuario autenticado envía el formulario de creación con datos válidos
- **THEN** el sistema crea el proyecto y asigna al autor actual

### Requirement: Any user can read published projects
El sistema SHALL permitir a cualquier usuario leer proyectos publicados.

#### Scenario: Read published project
- **WHEN** un usuario solicita un proyecto publicado por su slug
- **THEN** el sistema muestra el proyecto completo

### Requirement: Author can edit or delete their own project
El sistema SHALL permitir al autor de un proyecto editarlo o eliminarlo.

#### Scenario: Author edits own project
- **WHEN** el autor de un proyecto envía cambios válidos
- **THEN** el sistema actualiza el proyecto

#### Scenario: Author deletes own project
- **WHEN** el autor elimina su propio proyecto
- **THEN** el sistema elimina el proyecto y sus comentarios y likes asociados

### Requirement: Project views are counted
El sistema SHALL incrementar el contador de vistas cada vez que se accede a un proyecto publicado.

#### Scenario: Project view counter incremented
- **WHEN** un usuario accede a un proyecto publicado
- **THEN** el sistema incrementa el contador de vistas del proyecto en uno

### Requirement: Authenticated user can like or unlike a project
El sistema SHALL permitir a un usuario autenticado dar o quitar like a un proyecto.

#### Scenario: Like a project
- **WHEN** un usuario autenticado da like a un proyecto que no ha liked antes
- **THEN** el sistema registra el like y incrementa el contador de likes

#### Scenario: Unlike a project
- **WHEN** un usuario autenticado quita su like de un proyecto
- **THEN** el sistema elimina el like y decrementa el contador de likes

#### Scenario: Duplicate like prevented
- **WHEN** un usuario intenta dar like dos veces al mismo proyecto
- **THEN** el sistema registra solo un like

