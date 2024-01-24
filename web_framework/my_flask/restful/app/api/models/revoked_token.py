from . import db


class RevokedTokenModel(db.Model):
    """
    已过期的token表
    """

    __tablename__ = "revoked_tokens"

    # 主键 id
    id = db.Column(db.Integer, primary_key=True)
    # jwt 唯一标识
    jti = db.Column(db.String(120))

    # token 加黑
    def add(self):
        db.session.add(self)
        db.session.commit()

    # 查询是否是加黑的 token
    @classmethod
    def is_jti_blacklisted(cls, jti):
        query = cls.query.filter_by(jti=jti).first()
        return bool(query)
