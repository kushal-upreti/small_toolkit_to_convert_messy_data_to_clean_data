from tool_kit_level_0 import dict_list
from dataclasses import dataclass

csv_data_list = dict_list("messy_people.csv")

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

    def is_valid(self):
        value_list = [self.id, self.name, self.age, self.city, self.score]

        field_status = False

        for data in value_list:

            if data != "":
                field_status = True
            else:
                print(f"Row with Id {self.id} has missing values.")
                field_status = False
                return field_status
            
        return field_status


if __name__ == "__main__":
     
    recorded_obj = []

    for i in range(len(csv_data_list)):
        obj = Record((csv_data_list[i]['id']), (csv_data_list[i]['name']), (csv_data_list[i]['age']), (csv_data_list[i]['city']), (csv_data_list[i]['score']))
        obj.is_valid()
        recorded_obj.append(obj)

    print(recorded_obj[0].name)

