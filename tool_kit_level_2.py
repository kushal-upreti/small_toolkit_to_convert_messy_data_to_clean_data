import csv
from tool_kit_level_1 import Record

number_mapping = {
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9,
    "ten": 10,
    "eleven": 11,
    "twelve": 12,
    "thirteen": 13,
    "fourteen": 14,
    "fifteen": 15,
    "sixteen": 16,
    "seventeen": 17,
    "eighteen": 18,
    "nineteen": 19,
    "twenty": 20,
    "twenty one": 21,
    "twenty two": 22,
    "twenty three": 23,
    "twenty four": 24,
    "twenty five": 25,
    "twenty six": 26,
    "twenty seven": 27,
    "twenty eight": 28,
    "twenty nine": 29,
    "thirty": 30,
    "thirty one": 31,
    "thirty two": 32,
    "thirty three": 33,
    "thirty four": 34,
    "thirty five": 35,
    "thirty six": 36,
    "thirty seven": 37,
    "thirty eight": 38,
    "thirty nine": 39,
    "forty": 40
}


def mean(count: int, total:int | float) -> float:
    avg = total / count
    return avg

def findDuplicateID(filepath):
    with open(filepath, 'r') as csvfile:
    
        reader = csv.DictReader(csvfile)
        duplicates_ids = set()
        seen_ids = set()
        for row in reader:
            record_id = row['id'].strip()

            if record_id == '':
                continue

            if record_id in seen_ids:
                duplicates_ids.add(int(record_id))
            else:
                seen_ids.add(record_id)

    return duplicates_ids


class DataCleaning:

    def __init__(self):
        self.age_avg = None
        self.score_avg = None
        self.mode_name = None
        self.mode_city = None
        self.duplicate_ids = None

    def type_convert_and_word_to_num(self, data:dict) -> dict:
        for i in data:
            for key in number_mapping:
                if data[i] == key:
                    data[i] = number_mapping[key]

            try:
                if i == 'id' or i == 'age':
                    data[i] = int(data[i])
                elif i == 'score':
                    data[i] = float(data[i])

            except(ValueError):
                continue


    def statistics(self, filepath:str) -> tuple[DataCleaning, set]:
        count_age= 0
        count_score= 0
        sum_age= 0
        sum_score = 0
                
        with open(filepath, 'r') as csvfile:
            reader = csv.DictReader(csvfile)
            self.duplicate_ids = findDuplicateID(filepath)
            max_count_city = 0
            max_count_name = 0
            count_dict= {}

            for row in reader:

                self.type_convert_and_word_to_num(row)

                if row['id'] in self.duplicate_ids:
                    continue
                    
                if row['age'] != '':
                    count_age +=1
                    sum_age += row['age']

                if row['score'] != '':
                    count_score += 1
                    sum_score += row['score']


                # calcualte mode statistics of name and city
                city = row['city'].strip()
                name= row['name'].strip()

                if city != '':
                    count_dict[city] = count_dict.get(city, 0) +1
                    if  count_dict[city] > max_count_city:
                        max_count_city = count_dict[city]
                        self.mode_city = city

                if name != '':
                    count_dict[name] = count_dict.get(name, 0) +1
                    if  count_dict[name] > max_count_name:
                        max_count_name= count_dict[name]
                        self.mode_name = name                

            # calculate mean statistics
            self.age_avg = mean(count_age, sum_age)
            self.score_avg = mean(count_score, sum_score)

        return self

    def handle_missing_values(self, row:Record) ->Record:

        if row.age == '':
            row.age = self.age_avg

        if row.score == '':
            row.score = self.score_avg

        if row.name == '':
            row.name = self.mode_name

        if row.city == '':
            row.city = self.mode_city

