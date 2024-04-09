from flask import Blueprint
from flask_restful import Api

from .resources.login import Login
from .resources.logout import Logout
from .resources.register import Register
from .resources.user import UserService

# 统一管理api 所有接口的前缀为/api/xx
api_blueprint = Blueprint("api", __name__, url_prefix="/api")
api = Api(api_blueprint)


api.add_resource(Register, "/register")
api.add_resource(Login, "/login", "/refreshToken")
api.add_resource(
    Logout,
    "/logout",
)
api.add_resource(UserService, "/getUserList")
