from tool_kit_level_1 import Record
from tool_kit_level_2 import DataCleaning
import csv

filepath = "messy_people.csv"

class DataSet:

    def __init__(self, filepath):
        self.filepath = filepath
        self.obj_data_clean = DataCleaning()
        self.records = None



    def load(self):
        with open(self.filepath, 'r') as csvfile:
            reader = csv.DictReader(csvfile)

            for row in reader:
                yield row

    def clean_row(self, row:dict) -> Record:

        self.obj_data_clean.type_convert_and_word_to_num(row)
        self.obj_data_clean.statistics(self.filepath)
        duplicate_ids = self.obj_data_clean.duplicate_ids

        if not (row['age'] == '' and row['city'] == '' and row['score'] == ''):
        
            if not (row['id'] in duplicate_ids):
                self.records= Record(row['id'], row['name'], row['age'], row['city'], row['score'])

                if self.records.is_valid():
                    return self.records
                else:
                    self.obj_data_clean.handle_missing_values(self.records)
                    return self.records
                
            return None

    def iterate(self):

        for data in self.load():
            self.records = self.clean_row(data)

            yield self.records
        


obj = DataSet(filepath)

genrator = obj.iterate()

print(next(genrator))







             