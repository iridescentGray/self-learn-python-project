from flask_restful import Resource, reqparse
from flask_jwt_extended import (
    create_access_token,
    create_refresh_token,
    jwt_required,
    get_jwt_identity,
)

from werkzeug.security import check_password_hash

from ..schema.register_sha import reg_args_valid
from ..models.user import UserModel
from ..common.utils import res


# 生成token
def generateToken(id):
    access_token = create_access_token(identity=id)
    refresh_token = create_refresh_token(identity=id)
    return {
        "accessToken": "Bearer " + access_token,
        "refreshToken": "Bearer " + refresh_token,
    }


class Login(Resource):
    @jwt_required(refresh=True)
    def get(self):
        """用 refresh_token 来换取新的 token"""

        current_username = get_jwt_identity()
        access_token = create_access_token(identity=current_username)
        return res(data={"accessToken": "Bearer " + access_token})

    def post(self):
        # 初始化解析器
        parser = reqparse.RequestParser()
        # 添加请求参数校验
        reg_args_valid(parser)
        data = parser.parse_args()
        username = data["username"]
        user_tuple = UserModel.find_by_username(username)
        if user_tuple:
            try:
                (user,) = user_tuple
                pwd, salt = user.getPwd().get("pwd"), user.getPwd().get("salt")
                valid = check_password_hash(pwd, "{}{}".format(salt, data["pwd"]))
                if valid:
                    # 生成 token
                    response_data = generateToken(username)
                    return res(response_data)
                else:
                    raise ValueError("Invalid password!")
            except Exception as e:
                return res(success=False, message="Error: {}".format(e), code=500)
        else:
            return res(success=False, message="Unregistered username!", code=400)
