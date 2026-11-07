# Spec Delta

## Purpose

Organiza artículos y proyectos por ramas de ingeniería para facilitar el descubrimiento de contenido por especialidad.

## ADDED Requirements

### Requirement: Branch catalog exists
El sistema SHALL mantener un catálogo de ramas de ingeniería con nombre y slug únicos.

#### Scenario: Create branch
- **WHEN** un administrador crea una rama de ingeniería con nombre y slug válidos
- **THEN** el sistema registra la rama en el catálogo

#### Scenario: Duplicate branch slug rejected
- **WHEN** se intenta crear una rama con slug ya existente
- **THEN** el sistema rechaza la creación con un error de duplicado

### Requirement: Articles and projects are associated with a branch
El sistema SHALL permitir asociar cada artículo y proyecto a una rama de ingeniería.

#### Scenario: Article assigned to branch
- **WHEN** un autor crea o edita un artículo y selecciona una rama
- **THEN** el sistema asocia el artículo a esa rama

#### Scenario: Project assigned to branch
- **WHEN** un autor crea o edita un proyecto y selecciona una rama
- **THEN** el sistema asocia el proyecto a esa rama

### Requirement: Content is filterable by branch
El sistema SHALL permitir filtrar artículos y proyectos por rama de ingeniería.

#### Scenario: List articles by branch
- **WHEN** un usuario visita la página de una rama de ingeniería
- **THEN** el sistema muestra los artículos publicados de esa rama

#### Scenario: List projects by branch
- **WHEN** un usuario visita la página de una rama de ingeniería
- **THEN** el sistema muestra los proyectos publicados de esa rama

