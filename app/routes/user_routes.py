from flask import Blueprint
from app.controllers.user_controller import UserController

user_bp = Blueprint(
    "users",
    __name__
)

user_bp.route(
    "/users",
    methods=["POST"]
)(
    UserController.create
)

user_bp.route(
    "/users",
    methods=["GET"]
)(
    UserController.get_all
)

user_bp.route(
    "/users/<cedula>",
    methods=["GET"]
)(
    UserController.get_by_cedula
)

user_bp.route(
    "/users/<user_id>",
    methods=["DELETE"]
)(
    UserController.delete
)