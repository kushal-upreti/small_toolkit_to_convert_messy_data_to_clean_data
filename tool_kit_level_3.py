from tool_kit_level_1 import Record
from tool_kit_level_2 import DataCleaning
import csv


class DataSet:

    def __init__(self, filepath):
        self.filepath = filepath
        self.obj_data_clean = DataCleaning()
        self.records = None

        self.rows_loaded = 0
        self.rows_cleaned = 0
        self.rows_dropped = 0


        self.dropped_reasons = {
            "blank": 0,
            "duplicate_id": 0
        }        

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
            self.rows_loaded += 1

            self.records = self.clean_row(data)

            if self.records is None:

                self.rows_dropped += 1

                if (
                    data['age'] == ''
                    and data['city'] == ''
                    and data['score'] == ''
                ):
                    self.dropped_reasons["blank"] += 1

                elif data['id'] in self.obj_data_clean.duplicate_ids:
                    self.dropped_reasons["duplicate_id"] += 1

            else:
                self.rows_cleaned += 1
                yield self.records
        



             