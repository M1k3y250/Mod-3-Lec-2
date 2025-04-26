# Mod-3-Lec-2

Creación de la aplicación Flask: Se configuró una aplicación web con rutas básicas y estructura modular.

Definición de usuarios y roles: Se simularon usuarios con diferentes roles (admin y user), almacenando sus credenciales de forma segura (con hash).

Implementación de autenticación: Se usó Flask-Login para gestionar el inicio de sesión, cierre de sesión y sesiones de usuario.

Control de acceso por roles: Se integró Flask-Principal para autorizar el acceso a ciertas rutas según el rol del usuario.

Protección de rutas: Se crearon rutas exclusivas para cada tipo de usuario (/admin, /user, /dashboard) y se protegieron con decoradores de permisos.

Pruebas con REST Client: Se realizaron pruebas de acceso usando test.http para verificar el funcionamiento del sistema de autenticación y autorización.

Documentación: Se preparó evidencia del flujo del sistema mediante un diagrama, capturas de pantalla, y un repositorio con el código fuente.

![image](https://github.com/user-attachments/assets/000d34ce-8fd5-4162-af59-3e58923db7a0)
