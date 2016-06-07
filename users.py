import names
import random
import csv
from itertools import izip

def generate_random_names(num, gender_list):
    name_list = list()
    for x in range(0, num):
        name_list.append(names.get_full_name(gender=gender_list[x]))
    return name_list

def generate_random_ages(num):
    age_list = list()
    for x in range(0, num):
        age_list.append(random.randint(10,100))
    return age_list

def generate_random_genders(num):
    gender_list = list()
    genders = ['female', 'male']
    for x in range(0, num):
        gender_list.append(random.choice(genders))
    return gender_list

ids = range(1,101)
genders = generate_random_genders(100)
names = generate_random_names(100,genders)
ages = generate_random_ages(100)

with open('users.csv', 'wb') as myfile:
    wr = csv.writer(myfile)
    wr.writerows(izip(ids,names, ages, genders))

print names
print ages
print genders
