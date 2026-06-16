from app.models.user_model import UserModel
from app.repositories.user_repository import UserRepository

class UserService:

    @staticmethod
    def create_user(data):

        required = [
            "cedula",
            "nombres",
            "email"
        ]

        for field in required:

            if field not in data:
                raise ValueError(
                    f"{field} es obligatorio"
                )

        existing = UserRepository.get_by_cedula(
            data["cedula"]
        )

        if existing:
            raise ValueError(
                "La cédula ya existe"
            )

        user = UserModel.build(data)

        result = UserRepository.create(user)

        return str(result.inserted_id)

    @staticmethod
    def get_users():

        users = UserRepository.get_all()

        response = []

        for user in users:

            response.append({
                "id": str(user["_id"]),
                "cedula": user["cedula"],
                "nombres": user["nombres"],
                "email": user["email"]
            })

        return response

    @staticmethod
    def get_by_cedula(cedula):

        user = UserRepository.get_by_cedula(
            cedula
        )

        if not user:
            return None

        return {
            "id": str(user["_id"]),
            "cedula": user["cedula"],
            "nombres": user["nombres"],
            "email": user["email"]
        }

    @staticmethod
    def delete_user(user_id):

        result = UserRepository.delete(user_id)

        return result.deleted_count > 0