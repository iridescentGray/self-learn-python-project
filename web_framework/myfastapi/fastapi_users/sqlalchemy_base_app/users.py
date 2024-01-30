import typing
import os
from fastapi import Depends, Request
from fastapi_users import BaseUserManager, IntegerIDMixin, InvalidPasswordException
from sqlalchemy_base_app.model import UserCreate
from sqlalchemy_base_app.db import User, get_user_db
from fastapi_users.authentication import AuthenticationBackend, BearerTransport

SECRET = "SECRET"


"""
IntegerIDMixin doc:
https://fastapi-users.github.io/fastapi-users/12.1/configuration/user-manager/#the-id-parser-mixin


"""


class UserManager(IntegerIDMixin, BaseUserManager[User, int]):
    reset_password_token_secret = SECRET
    verification_token_secret = SECRET

    async def on_after_register(
        self, user: User, request: typing.Optional[Request] = None
    ):
        print(f"User {user.id} has registered.")

    async def on_after_forgot_password(
        self, user: User, token: str, request: typing.Optional[Request] = None
    ):
        print(f"User {user.id} has forgot their password. Reset token: {token}")

    async def on_after_request_verify(
        self, user: User, token: str, request: typing.Optional[Request] = None
    ):
        print(f"Verification requested for user {user.id}. Verification token: {token}")

    async def validate_password(
        self,
        password: str,
        user: typing.Union[UserCreate, User],
    ) -> None:
        if len(password) < 6:
            raise InvalidPasswordException(
                reason="Password should be at least 8 characters"
            )
        if user.email in password:
            raise InvalidPasswordException(reason="Password should not contain e-mail")


async def get_user_manager(user_db=Depends(get_user_db)):
    yield UserManager(user_db)


from strategy.database_strategy import get_database_strategy

db_bearer_transport = BearerTransport(tokenUrl="auth/db/login")
db_auth_backend = AuthenticationBackend(
    name="db",
    transport=db_bearer_transport,
    get_strategy=get_database_strategy,
)

from strategy.jwt_strategy import get_jwt_strategy

jwt_bearer_transport = BearerTransport(tokenUrl="auth/jwt/login")
jwt_auth_backend = AuthenticationBackend(
    name="jwt",
    transport=jwt_bearer_transport,
    get_strategy=get_jwt_strategy,
)


from strategy.redis_strategy import get_redis_strategy

redis_bearer_transport = BearerTransport(tokenUrl="auth/redis/login")


redis_auth_backend = AuthenticationBackend(
    name="redis",
    transport=redis_bearer_transport,
    get_strategy=get_redis_strategy,
)

from fastapi_users import FastAPIUsers

fastapi_users = FastAPIUsers[User, int](get_user_manager, [jwt_auth_backend])


# doc: https://fastapi-users.github.io/fastapi-users/12.1/usage/current-user/
current_active_user = fastapi_users.current_user(active=True)


from httpx_oauth.clients.google import GoogleOAuth2

google_oauth_client = GoogleOAuth2(
    os.getenv("GOOGLE_OAUTH_CLIENT_ID", ""),
    os.getenv("GOOGLE_OAUTH_CLIENT_SECRET", ""),
)
