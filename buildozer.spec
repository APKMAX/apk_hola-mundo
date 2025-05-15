[app]

# Título de la aplicación
title = HolaMundo

# Nombre del paquete (debe ser único)
package.name = holamundo

# Dominio (formato inverso, ej: com.tudominio)
package.domain = com.ejemplo

# Versión obligatoria (formato: 0.1)
version = 0.1

# Carpeta del código fuente
source.dir = .

# Archivos a incluir (extensiones permitidas)
source.include_exts = py,png,jpg,kv,ttf

# Dependencias
requirements = python3, kivy

# Permisos de Android (opcional)
android.permissions = INTERNET

# Aceptar licencias automáticamente (evita prompts)
android.accept_sdk_license = True

# Versión mínima de Android
android.sdk = 24

# Rama de Python para Android (recomendada para Kivy)
p4a.branch = develop

# Log nivel detallado (útil para debug)
log_level = 2