from pydantic import BaseModel, ConfigDict, ValidationError, Field

print(f"-----------------------------------------Generator Alias------------------------------------------")


def to_camel(string: str) -> str:
    return ''.join(word.capitalize() for word in string.split('_'))


class Voice(BaseModel):
    model_config = ConfigDict(alias_generator=to_camel)

    name: str
    language_code: str


voice1 = Voice(Name='Filiz', LanguageCode='tr-TR')
print(voice1.model_dump())
print(voice1.model_dump(by_alias=True))

try:
    voice2 = Voice(name='Bob', language_code='n-TR')
except ValidationError as e:
    print(e)

print(f"-----------------------------------------Alias Precedence------------------------------------------")


class VoiceWithAliasField(BaseModel):
    model_config = ConfigDict(alias_generator=to_camel)

    name: str
    # Field(alias='lang') is precedence than model_config
    language_code: str = Field(alias='lang')


voice_with_alias = VoiceWithAliasField(Name='Filiz', lang='tr-TR')
print(voice_with_alias.language_code)
print(voice_with_alias.model_dump(by_alias=True))


print(f"--------------------------------Allow User Original Name After Set Alias-----------------------------------")

class User(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    name: str = Field(alias='full_name')
    age: int


user = User(full_name='John Doe', age=20)
print(user)
# allowed by ConfigDict(populate_by_name=True)
user = User(name='John Doe', age=20)
print(user)

