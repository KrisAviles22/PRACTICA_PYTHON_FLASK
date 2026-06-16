# Microservicio de Gestión de Usuarios
Se desarrolló un microservicio para la gestión de usuarios utilizando Python y Flask.
## Tecnologías utilizadas
- Python
- Flask
- Gunicorn
- MongoDB
- Docker
- Postman
# Funcionalidades
## Crear usuarios
## Consultar usuarios mediante cédula
# Ejecución del proyecto
1. Clonar el repositorio
2. Construir los contenedores
docker compose up --build
3. Ejecutar el servicio
Una vez iniciado el contenedor, el microservicio quedará disponible en el puerto configurado en la aplicación.
Pruebas
Las pruebas de los endpoints fueron realizadas mediante Postman para verificar el correcto funcionamiento.
# Endpoints disponibles
1. Crear usuario
POST /api/v1/users
Crea un nuevo usuario en la base de datos.
Body de ejemplo:
{
  "cedula": "0912345670",
  "nombres": "Kristier Zambrano",
  "email": "milena@outlook.com"
}
Response:
{
    "id": "6a31c0fa7a768d65a5d0954e",
    "message": "Usuario creado"
}

2. Obtener todos los usuarios
GET /api/v1/users
Response
    {
        "cedula": "0912345678",
        "email": "kristier@test.com",
        "id": "6a30c751e623d515faa34d23",
        "nombres": "Kristier Zambrano"
    },
    {
        "cedula": "0912345648",
        "email": "milena@test.com",
        "id": "6a30d1ca3fe5ce2973ff13a2",
        "nombres": "Milena Zambrano"
    },
    {
        "cedula": "0912345670",
        "email": "milena@outlook.com",
        "id": "6a31c0fa7a768d65a5d0954e",
        "nombres": "Kristier Zambrano"
    }
4. Consultar usuario por cédula
GET /api/v1/users/1723456789
Response
{
    "cedula": "0912345678",
    "email": "kristier@test.com",
    "id": "6a30c751e623d515faa34d23",
    "nombres": "Kristier Zambrano"
}

5. Eliminar usuario
DELETE /api/v1/users/684f9a1b2c3d4e5f67890123
Response
{
    "message": "Usuario eliminado correctamente"
}
