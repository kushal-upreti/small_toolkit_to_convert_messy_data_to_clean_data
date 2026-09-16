import csv
import matplotlib.pyplot as plt
from tool_kit_level_1 import Record

with open("messy_people.csv", 'r') as csvfile:
    csv_reader = csv.DictReader(csvfile)
    csv_dict_list = list(csv_reader)

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

""""
min = 28
max= 28

for i in range(len(dict_list)):

    try:
        if dict_list[i]['age'] == 'thirty' or dict_list[i]['age'] == '':

            if max <= int(dict_list[i+1]['age']):
                max = int(dict_list[i+1]['age'])

            if min >= int(dict_list[i+1]['age']):
                min = int(dict_list[i+1]['age'])

        else:
            if max <= int(dict_list[i]['age']):
                max = int(dict_list[i]['age'])

            if min >= int(dict_list[i]['age']):
                min = int(dict_list[i]['age'])           

    except Exception as e:
        print(e)


print(max, min) """

def mean(age):
    try:
        sum = 0
        for data in age:
            sum += data
        avg = sum / len(age)

        return avg
    except (ValueError, TypeError):
        print ("int or float datatype is required to process mean")


def iqr_range(data_list):
    try:
        data_list.sort()
        n= len(data_list)

        if n % 2 == 0 or n % 4 == 0:
            median = (data_list[n//2-1] + data_list[(n//2)])/2
            q1 = (data_list[n//4-1]) + (((n/4)-(n//4)) *(data_list[(n//4)]-data_list[n//4-1]))
            q3 = (data_list[(3*n)//4-1]) + (((3*n)/4)-((3*n)//4)) *(data_list[((3*n)//4)]-data_list[((3*n)//4)-1])
        else:
            median = data_list[(n)//2]
            q1 = data_list[n//4]
            q3 = data_list[(3*n)//4]

        lb = q1 - ((1.5) *(q3-q1))
        ub = q3 + ((1.5) *(q3-q1))

        return lb ,ub, median
    except ValueError:
        return ("datatype is string or consist empty string so Lb and ub canot be calculated")
    

def mode(data_list):

    mode_value = ['sarlahi', 1]
    for i in range(len(data_list)):
        counter = 1
        for j in range(1,len(data_list)):
            if data_list[i].lower() == data_list[j].lower():
                counter +=1

        if counter > mode_value[1]:
            mode_value[0] = (data_list[i])
            mode_value[1] = (counter)

    return mode_value


def type_conversion():

    for i in range(len(csv_dict_list)):
    
        for key in number_mapping:

            if csv_dict_list[i]['age'].lower() == key.lower():
                csv_dict_list[i]['age']= str(number_mapping[key])

        if csv_dict_list[i]['age'] != '':
            csv_dict_list[i]['age'] = int(csv_dict_list[i]['age'])

        if csv_dict_list[i]['id'] != '':
            csv_dict_list[i]['id'] = int(csv_dict_list[i]['id'])

        if csv_dict_list[i]['score'] != '':
            csv_dict_list[i]['score'] = float(csv_dict_list[i]['score'])


def check_outlier(csv_dict_list, lb, ub, key:str):
    outlier = []

    for i in range(len(csv_dict_list)):

        if csv_dict_list[i][key] == '':
            continue

        elif csv_dict_list[i][key] >ub:
            outlier.append(csv_dict_list[i][key])

        elif csv_dict_list[i][key] < lb:
            outlier.append(csv_dict_list[i][key])

    if not outlier:
        print(f'no outlier exist {key} column data')

    else:
        print("There is an outlier value. Please do furhter check on that value")
        
    return outlier


def handle_missing_values(csv_dict_list, mode_value_city, mode_value_name):

    for i in range(len(csv_dict_list)-1 , -1, -1):

        if csv_dict_list[i]['age'] == '' and csv_dict_list[i]['city'] == '' and csv_dict_list[i]['score'] == '':
            del(csv_dict_list[i])

        if csv_dict_list[i]['age'] == '':
            csv_dict_list[i]['age'] = age_avg

        if csv_dict_list[i]['score'] == '':
            csv_dict_list[i]['score'] = score_avg

        if csv_dict_list[i]['city'] == '':
            csv_dict_list[i]['city'] = mode_value_city[0]

        if csv_dict_list[i]['name'] == '':
            csv_dict_list[i]['name'] = mode_value_name[0]

    return csv_dict_list

# def removeDuplicates(csv_dict_list):
#     data_list = csv_dict_list

#     for i in range(len(data_list)):
#         del(data_list[i]['id'])
#         del(data_list[i]['name'])
#         (hash(data_list[i]['age']))
#         (hash(data_list[i]['city']))
#         (hash(data_list[i]['score']))

#     print(data_list)


type_conversion()

age_list = [(csv_dict_list[i]['age']) for i in range(len(csv_dict_list)) if csv_dict_list[i]['age'] != '']
score_list = [(csv_dict_list[i]['score']) for i in range(len(csv_dict_list)) if csv_dict_list[i]['score'] != '']
name_list = [(csv_dict_list[i]['name']) for i in range(len(csv_dict_list)) if csv_dict_list[i]['name'] != '']
city_list = [(csv_dict_list[i]['city']) for i in range(len(csv_dict_list)) if csv_dict_list[i]['city'] != '']


age_avg= round(mean(age_list))
score_avg= (mean(score_list))

age_lb, age_ub, age_median = (iqr_range(age_list))
score_lb, score_ub, score_median = (iqr_range(score_list))

outlier_data_age = check_outlier(csv_dict_list, age_lb, age_ub, 'age')
outlier_data_score = check_outlier(csv_dict_list, score_lb, score_ub, 'score')

handle_missed_Values = handle_missing_values(csv_dict_list, mode(city_list), mode(name_list))








# plt.hist(score_list)
# plt.xlabel("age")
# plt.ylabel('frequency')
# plt.show()

for i in range(len(csv_dict_list)):
    csv_dict_list[i]['id'] = i+1


recorded_obj = []
for i in range(len(csv_dict_list)):
    obj = Record((csv_dict_list[i]['id']), (csv_dict_list[i]['name']), (csv_dict_list[i]['age']), (csv_dict_list[i]['city']), (csv_dict_list[i]['score']))
    recorded_obj.append(obj)

recorded_obj[0].name = ''

print(recorded_obj[0].name)

for i in range(len(recorded_obj)):
    if not recorded_obj[i].is_valid():
        status = False

if status:
    print("data is clean")


# removeDuplicates(csv_dict_list)
# print('age_avg: ', age_avg)
# print('age_median: ', age_median)
# print('score_Avg', score_avg)
# print('score median: ', score_median)
# print('score_q1: ', score_q1)
# print('score_q3: ', score_q3)

