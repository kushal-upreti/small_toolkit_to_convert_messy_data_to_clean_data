from tool_kit_level_3 import DataSet
from tool_kit_level_4 import analyze
from tool_kit_level_5 import Report

filepath = 'messy_people.csv'
dataset = DataSet(filepath)

average, city_count, oldest_person, youngest_person = analyze(dataset)

report = Report(
    dataset,
    average,
    city_count,
    oldest_person,
    youngest_person
)

report.display()