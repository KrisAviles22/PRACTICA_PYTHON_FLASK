from flask import request, jsonify
from app.services.user_service import UserService

class UserController:

    @staticmethod
    def create():

        try:

            user_id = UserService.create_user(
                request.json
            )

            return jsonify({
                "message": "Usuario creado",
                "id": user_id
            }), 201

        except Exception as e:

            return jsonify({
                "error": str(e)
            }), 400

    @staticmethod
    def get_all():

        return jsonify(
            UserService.get_users()
        )

    @staticmethod
    def get_by_cedula(cedula):

        user = UserService.get_by_cedula(
            cedula
        )

        if not user:

            return jsonify({
                "error": "No encontrado"
            }), 404

        return jsonify(user)

    @staticmethod
    def delete(user_id):

        deleted = UserService.delete_user(
            user_id
        )

        if not deleted:

            return jsonify({
                "error": "No encontrado"
            }), 404

        return jsonify({
            "message": "Usuario eliminado"
        })