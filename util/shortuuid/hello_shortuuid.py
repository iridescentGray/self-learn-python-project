print(
    "---------------------------------base useage---------------------------------------"
)
import uuid

print(uuid.uuid4())  # python build-in module

import shortuuid

print(shortuuid.uuid())  # more short

print(
    "------------------------------generation uuid from str-------------------------------"
)
print(shortuuid.uuid(name="<http://example.com>"))  # ensure generation everytime equal

print(
    "----------------------------Specify uuid length---------------------------------------"
)
print(shortuuid.ShortUUID().random(5))
print(shortuuid.ShortUUID().random(10))
print(shortuuid.ShortUUID().random(20))


print(
    "--------------------------Output/Set characters used to generate uuids-------------------------"
)
print(shortuuid.get_alphabet())
shortuuid.set_alphabet("abcdefg")
print(shortuuid.uuid())

print(
    "---------------------set_alphabet don't affect ShortUUID generation----------------------"
)
print(shortuuid.ShortUUID().random(20))
print(
    shortuuid.ShortUUID(alphabet="bcdefg").random(20)
)  # ShortUUID need Manual development alphabet


print(
    "------------------------------------serialize existing UUIDs--------------------------------"
)
u = uuid.uuid4()
s = shortuuid.encode(u)
print(u)  # cf502b50-f75d-4f36-94a9-6bd04789ca55
print(s)  # etUe7amvdJvHQY6Emf2TiL
print(shortuuid.decode(s) == u)  # True
