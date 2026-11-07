# Spec Delta

## Purpose

Gestiona el acceso de usuarios a la plataforma: registro, autenticación, perfiles con profesión y administración de cuentas.

## ADDED Requirements

### Requirement: User can register
El sistema SHALL permitir a un usuario nuevo registrarse con nombre de usuario, email, contraseña y profesión.

#### Scenario: Successful registration
- **WHEN** un usuario envía el formulario de registro con datos válidos y email único
- **THEN** el sistema crea la cuenta, autentica al usuario y redirige a su perfil

#### Scenario: Duplicate email rejected
- **WHEN** un usuario intenta registrarse con un email ya existente
- **THEN** el sistema rechaza el registro y muestra un error de email duplicado

### Requirement: User can log in and out
El sistema SHALL permitir a un usuario registrado iniciar y cerrar sesión.

#### Scenario: Successful login
- **WHEN** un usuario envía credenciales válidas
- **THEN** el sistema inicia sesión y redirige al home

#### Scenario: Invalid credentials rejected
- **WHEN** un usuario envía credenciales inválidas
- **THEN** el sistema rechaza el acceso y muestra un error de autenticación

#### Scenario: Logout clears session
- **WHEN** un usuario autenticado cierra sesión
- **THEN** el sistema invalida la sesión y redirige al home

### Requirement: User profile includes profession
El sistema SHALL almacenar y mostrar la profesión del usuario en su perfil público.

#### Scenario: Profession displayed on profile
- **WHEN** se visita el perfil público de un usuario
- **THEN** el sistema muestra la profesión declarada por ese usuario

### Requirement: Admin manages users
El sistema SHALL permitir a un administrador gestionar usuarios desde el admin de Django.

#### Scenario: Admin creates user
- **WHEN** un administrador crea un usuario desde el admin de Django
- **THEN** el sistema registra el nuevo usuario en la base de datos

