from flask_jwt_extended import get_jwt, jwt_required
from flask_restful import Resource

from ..common.utils import res
from ..models.revoked_token import RevokedTokenModel


class Logout(Resource):
    @jwt_required()
    def post(self):
        jti = get_jwt()["jti"]
        try:
            # 用户退出系统时 将 token 加入黑名单
            revoked_token = RevokedTokenModel(jti=jti)  # type: ignore
            revoked_token.add()
            return res()
        except Exception:
            return res(success=False, message="服务器繁忙！", code=500)
