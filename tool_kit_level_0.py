import csv

# ***************Level 0 ---> Task Load and Loook******************

filepath = "/data/Files/Intern_Docs/Task_3/messy_people.csv"

def dict_list(filepath):
    people_messy_csv = open(filepath)

    csv_data = csv.DictReader(people_messy_csv)

    csv_dict_list = list(csv_data)
    return csv_dict_list


if __name__ == "__main__":
    csv_data_list = dict_list(filepath)

    for i in range(len(csv_data_list)):
        if i > 2:
            break
        print(csv_data_list[i])

    print(len(csv_data_list))