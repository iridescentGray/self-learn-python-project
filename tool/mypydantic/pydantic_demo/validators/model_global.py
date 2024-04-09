from pydantic import BaseModel, ValidationError, model_validator


class UserModel(BaseModel):
    username: str
    password1: str
    password2: str

    # called before field validation
    @model_validator(mode="before")
    def check_card_number_omitted(cls, data):
        assert "card_number" not in data, "card_number should not be included"
        return data

    # called after field validation
    @model_validator(mode="after")
    def check_passwords_match(self) -> "UserModel":
        pw1 = self.password1
        pw2 = self.password2
        if pw1 is not None and pw2 is not None and pw1 != pw2:
            raise ValueError("passwords do not match")
        return self


print(UserModel(username="scolvin", password1="zxcvbn", password2="zxcvbn"))
try:
    UserModel(username="scolvin", password1="zxcvbn", password2="zxcvbn2")
except ValidationError as e:
    print(e)

try:
    UserModel(
        username="scolvin",
        password1="zxcvbn",
        password2="zxcvbn",
        card_number="1234",
    )
except ValidationError as e:
    print(e)
