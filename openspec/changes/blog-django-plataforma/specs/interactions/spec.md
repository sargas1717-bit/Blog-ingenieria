# Spec Delta

## Purpose

Gestiona las interacciones de usuarios con contenido: likes en proyectos y conteo atómico de vistas.

## ADDED Requirements

### Requirement: Project like is atomic and unique per user
El sistema SHALL garantizar que un usuario solo pueda dar un like por proyecto y que el contador sea consistente bajo concurrencia.

#### Scenario: Concurrent likes do not double count
- **WHEN** dos usuarios dan like al mismo proyecto simultáneamente
- **THEN** el contador de likes se incrementa exactamente en dos

#### Scenario: Unique like constraint enforced
- **WHEN** un usuario intenta dar like al mismo proyecto dos veces
- **THEN** el sistema registra solo un like

### Requirement: View count increment is atomic
El sistema SHALL incrementar contadores de vistas de forma atómica para evitar pérdida de actualizaciones bajo concurrencia.

#### Scenario: Concurrent views counted correctly
- **WHEN** múltiples usuarios acceden al mismo artículo simultáneamente
- **THEN** el contador de vistas refleja todas las visitas sin pérdida

