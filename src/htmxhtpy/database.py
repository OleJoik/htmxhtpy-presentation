from typing import Literal, TypedDict


class LotrCharacter(TypedDict):
    name: str
    age: int
    gender: Literal["Male", "Female"]
    people: str


def query(data, skip, take):
    if skip >= len(data):
        return []
    return data[skip : skip + take]


data: list[LotrCharacter] = [
    {"name": "Aragorn", "age": 210, "gender": "Male", "people": "Human"},
    {"name": "Legolas", "age": 2931, "gender": "Male", "people": "Elf"},
    {"name": "Gimli", "age": 139, "gender": "Male", "people": "Dwarf"},
    {"name": "Gollum", "age": 589, "gender": "Male", "people": "Hobbit"},
    {"name": "Galadriel", "age": 8372, "gender": "Female", "people": "Elf"},
    {"name": "Frodo Baggins", "age": 53, "gender": "Male", "people": "Hobbit"},
    {"name": "Saruman", "age": 2019, "gender": "Male", "people": "Maiar"},
    {"name": "Sauron", "age": 50000, "gender": "Male", "people": "Maiar"},
    {"name": "Eowyn", "age": 24, "gender": "Female", "people": "Human"},
    {"name": "Boromir", "age": 41, "gender": "Male", "people": "Human"},
    {"name": "Samwise Gamgee", "age": 39, "gender": "Male", "people": "Hobbit"},
    {"name": "Elrond", "age": 6518, "gender": "Male", "people": "Elf"},
    {"name": "Thranduil", "age": 4000, "gender": "Male", "people": "Elf"},
    {"name": "Faramir", "age": 36, "gender": "Male", "people": "Human"},
    {"name": "Grima Wormtongue", "age": 53, "gender": "Male", "people": "Human"},
    {"name": "Theoden", "age": 71, "gender": "Male", "people": "Human"},
    {"name": "Bilbo Baggins", "age": 131, "gender": "Male", "people": "Hobbit"},
    {"name": "Merry Brandybuck", "age": 36, "gender": "Male", "people": "Hobbit"},
    {"name": "Peregrin Took", "age": 28, "gender": "Male", "people": "Hobbit"},
    {"name": "Treebeard", "age": 17000, "gender": "Male", "people": "Ent"},
    {"name": "Radagast", "age": 2019, "gender": "Male", "people": "Maiar"},
    {"name": "Denethor", "age": 89, "gender": "Male", "people": "Human"},
    {"name": "Arwen", "age": 2778, "gender": "Female", "people": "Elf"},
    {"name": "Isildur", "age": 234, "gender": "Male", "people": "Human"},
    {"name": "Glorfindel", "age": 7000, "gender": "Male", "people": "Elf"},
    {"name": "Haldir", "age": 2000, "gender": "Male", "people": "Elf"},
    {"name": "Gothmog", "age": 3000, "gender": "Male", "people": "Orc"},
    {"name": "Lurtz", "age": 10, "gender": "Male", "people": "Uruk-hai"},
    {"name": "Shelob", "age": 7000, "gender": "Female", "people": "Spider"},
    {"name": "Eomer", "age": 28, "gender": "Male", "people": "Human"},
    {"name": "Balin", "age": 231, "gender": "Male", "people": "Dwarf"},
    {"name": "Dain Ironfoot", "age": 252, "gender": "Male", "people": "Dwarf"},
    {"name": "Bard the Bowman", "age": 93, "gender": "Male", "people": "Human"},
    {"name": "Beorn", "age": 250, "gender": "Male", "people": "Skin-changer"},
    {"name": "Grima Wormtongue", "age": 53, "gender": "Male", "people": "Human"},
    {"name": "Theoden", "age": 71, "gender": "Male", "people": "Human"},
    {"name": "Bilbo Baggins", "age": 131, "gender": "Male", "people": "Hobbit"},
    {"name": "Merry Brandybuck", "age": 36, "gender": "Male", "people": "Hobbit"},
    {"name": "Peregrin Took", "age": 28, "gender": "Male", "people": "Hobbit"},
    {"name": "Treebeard", "age": 17000, "gender": "Male", "people": "Ent"},
    {"name": "Radagast", "age": 2019, "gender": "Male", "people": "Maiar"},
    {"name": "Denethor", "age": 89, "gender": "Male", "people": "Human"},
    {"name": "Arwen", "age": 2778, "gender": "Female", "people": "Elf"},
    {"name": "Isildur", "age": 234, "gender": "Male", "people": "Human"},
    {"name": "Glorfindel", "age": 7000, "gender": "Male", "people": "Elf"},
    {"name": "Haldir", "age": 2000, "gender": "Male", "people": "Elf"},
    {"name": "Gothmog", "age": 3000, "gender": "Male", "people": "Orc"},
    {"name": "Lurtz", "age": 10, "gender": "Male", "people": "Uruk-hai"},
    {"name": "Shelob", "age": 7000, "gender": "Female", "people": "Spider"},
    {"name": "Eomer", "age": 28, "gender": "Male", "people": "Human"},
    {"name": "Balin", "age": 231, "gender": "Male", "people": "Dwarf"},
    {"name": "Dain Ironfoot", "age": 252, "gender": "Male", "people": "Dwarf"},
    {"name": "Bard the Bowman", "age": 93, "gender": "Male", "people": "Human"},
    {"name": "Beorn", "age": 250, "gender": "Male", "people": "Skin-changer"},
]
