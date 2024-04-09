from pydantic import RootModel

# root model is the Way To Custom Definition Model
print(
    f"-----------------------------------------list Root Model------------------------------------------"
)

Pets = RootModel[list[str]]
pet = Pets(["dog", "cat"])
print(pet)
print(pet.model_dump_json())
print(Pets.model_validate(["dog", "cat"]))
print(Pets.model_json_schema())

print(
    f"-----------------------------------------------dict Root Model--------------------------------------------"
)

PetsByName = RootModel[dict[str, str]]
print(PetsByName({"Otis": "dog", "Milo": "cat"}))
print(PetsByName({"Otis": "dog", "Milo": "cat"}).model_dump_json())
print(PetsByName.model_validate({"Otis": "dog", "Milo": "cat"}))

print(
    f"-----------------------------------------Iterable Root Model------------------------------------------"
)


class IterablePets(RootModel):
    root: list[str]

    def __iter__(self):
        return iter(self.root)

    def __getitem__(self, item):
        return self.root[item]


pets = IterablePets.model_validate(["dog", "cat"])
print(pets[0])
for pet in pets:
    print(pet)

print(
    "-----------------------------------------subclass Root Model------------------------------------------"
)


class Pets(RootModel[list[str]]):
    root: list[str]

    def describe(self) -> str:
        return f'Pets: {", ".join(self.root)}'


my_pets = Pets.model_validate(["dog", "cat"])

print(my_pets.describe())
