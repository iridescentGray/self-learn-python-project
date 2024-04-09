from flask_jwt_extended import jwt_required
from flask_restful import Resource

from ..common.utils import res
from ..models.user import UserModel


class UserService(Resource):
    @jwt_required()
    def get(self):
        userList = UserModel.get_all_user()
        result = []
        for user in userList:
            result.append(user.dict())

        return res(data=result)
