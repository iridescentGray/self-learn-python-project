from flask_restful import Resource
from flask_jwt_extended import jwt_required, get_jwt
from ..models.revoked_token import RevokedTokenModel
from ..common.utils import res


class Logout(Resource):
    @jwt_required()
    def post(self):
        jti = get_jwt()["jti"]
        try:
            # 用户退出系统时 将 token 加入黑名单
            revoked_token = RevokedTokenModel(jti=jti)  # type: ignore
            revoked_token.add()
            return res()
        except:
            return res(success=False, message="服务器繁忙！", code=500)
