import csv

# ***************Level 0 ---> Task Load and Loook******************

filepath = "/data/Files/Intern_Docs/Task_3/messy_people.csv"

people_messy_csv = open(filepath)

csv_data = csv.DictReader(people_messy_csv)

dict_list = list(csv_data)

for i in range(len(dict_list)):
    if i > 2:
        break
    print(dict_list[i])

print(len(dict_list))