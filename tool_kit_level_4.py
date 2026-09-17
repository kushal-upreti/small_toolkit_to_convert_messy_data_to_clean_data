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
def analyze(dataset: DataSet) -> tuple[float, dict, Record, Record]:

    total_score = 0
    count = 0
    city_count = {}

    oldest = None
    youngest = None

    for record in dataset.iterate():
        if record is None:
            continue

        total_score += record.score
        count += 1

        city_count[record.city] = city_count.get(record.city, 0) + 1

        if oldest is None or record.age > oldest.age:
            oldest = record

        if youngest is None or record.age < youngest.age:
            youngest = record

    average_score = total_score / count

    return average_score, city_count, oldest, youngest