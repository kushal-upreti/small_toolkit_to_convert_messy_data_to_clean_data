import csv
import matplotlib.pyplot as plt

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
    sum = 0
    for data in age:
        sum += data
    avg = sum / len(age)

    return avg

def iqr_range(data_list):
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

    return median, q1, q3

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

for i in range(len(csv_dict_list)):

    for key in number_mapping:
        if csv_dict_list[i]['age'].lower() == key.lower():
            csv_dict_list[i]['age']= str(number_mapping[key])

    if csv_dict_list[i]['age'] != '':
        csv_dict_list[i]['age'] = int(csv_dict_list[i]['age'])

    if csv_dict_list[i]['score'] != '':
        csv_dict_list[i]['score'] = float(csv_dict_list[i]['score'])

age_list = [(csv_dict_list[i]['age']) for i in range(len(csv_dict_list)) if csv_dict_list[i]['age'] != '']
score_list = [(csv_dict_list[i]['score']) for i in range(len(csv_dict_list)) if csv_dict_list[i]['score'] != '']
name_list = [(csv_dict_list[i]['name']) for i in range(len(csv_dict_list)) if csv_dict_list[i]['name'] != '']
city_list = [(csv_dict_list[i]['city']) for i in range(len(csv_dict_list)) if csv_dict_list[i]['city'] != '']



age_avg= round(mean(age_list))
score_avg= round(mean(score_list))

age_median, age_q1, age_q3 = (iqr_range(age_list))
score_median, score_q1, score_q3 = (iqr_range(score_list))

mode_value_name = mode(name_list)
mode_value_city = mode(city_list)


lb = score_q1 - ((1.5) *(score_q3-score_q1))
ub = score_q3 + ((1.5) *(score_q3-score_q1))

lb_age = age_q1 - ((1.5) *(age_q3-age_q1))
ub_age= age_q3 + ((1.5) *(age_q3-age_q1))

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




# plt.hist(score_list)
# plt.xlabel("age")
# plt.ylabel('frequency')
# plt.show()

print(csv_dict_list)


# ***********Outlier check*********************
# outlier = []
# outlier_age = []

# for i in range(len(csv_dict_list)):
#     if csv_dict_list[i]['score'] == '':
#         continue
#     elif csv_dict_list[i]['score'] >ub:
#         outlier.append(csv_dict_list[i]['score'])
#     elif csv_dict_list[i]['score'] < lb:
#         outlier.append(csv_dict_list[i]['score'])

# for i in range(len(csv_dict_list)):
#     if csv_dict_list[i]['age'] == '':
#         continue
#     elif csv_dict_list[i]['age'] >ub_age:
#         outlier_age.append(csv_dict_list[i]['age'])
#     elif csv_dict_list[i]['age'] < lb_age:
#         outlier_age.append(csv_dict_list[i]['age'])

# if not outlier:
#     print('no outlier in score')
           
# if not outlier_age:
#     print('no outlier in age')


# print('age_avg: ', age_avg)
# print('age_median: ', age_median)
# print('score_Avg', score_avg)
# print('score median: ', score_median)
# print('score_q1: ', score_q1)
# print('score_q3: ', score_q3)

