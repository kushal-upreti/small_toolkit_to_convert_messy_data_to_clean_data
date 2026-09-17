from dataclasses import dataclass
# -------------Record class using normal init constructor---------------------

# class Record:

#     def __init__(self, id, name, age, city, score):
#         self.id = id
#         self.name = name
#         self.age = age
#         self.city = city
#         self.score = score

# -------Record class using dataclass decorator-----------
@dataclass
class Record:
    id : int
    name: str
    age : int
    city: str
    score: float

    def is_valid(self) -> bool:
        value_list = [self.id, self.name, self.age, self.city, self.score]

        for data in value_list:

            if data == "":
                return False

        return True

