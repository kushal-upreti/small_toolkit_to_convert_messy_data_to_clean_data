from tool_kit_level_3 import DataSet
from tool_kit_level_1 import Record
import time

def log_call(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs )
        end_time = time.time()

        print(f"{func.__name__} took {end_time - start_time:.6f} seconds")

        return result
    return wrapper

@log_call
def average_score(dataset: DataSet) -> float:
    total_score = 0
    count = 0

    for record in dataset.iterate():
        if record is None:
            continue
        total_score += record.score
        count += 1

    if count == 0:
        return 0
    
    return total_score / count

@log_call
def people_per_city(dataset:DataSet) -> dict:
    city_count = {}
    for record in dataset.iterate():
        if record is None:
            continue

        if record.city not in city_count:
            city_count[record.city] = 0

        city_count[record.city] += 1

    return city_count

@log_call
def oldest(dataset: DataSet) -> Record:
    oldest = None
    for record in dataset.iterate():

        if record is None:
            continue

        if oldest is None or record.age > oldest.age:
            oldest = record

    return oldest

@log_call
def youngest(dataset:DataSet) -> Record:
    youngest = None
    for record in dataset.iterate():

        if record is None:
            continue

        if youngest is None or record.age < youngest.age:
            youngest = record

    return youngest
