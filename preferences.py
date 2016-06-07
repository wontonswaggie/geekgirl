import csv
import random

users = []
music = []
preferences = []
probabilities = {};

with open('music.csv', 'rU') as mf:
    reader = csv.reader(mf)
    for row in reader:
        music.append({'id': row[0], 'name': row[1], 'artist': row[2],
                        'tempo': row[3],'genre': row[2]})

with open('users.csv', 'rU') as uf:
    reader = csv.reader(uf)
    for row in reader:
        users.append({'id': row[0], 'name': row[1], 'age': row[2], 'gender': row[3]})

def flip(p):
    return 'H' if random.random() < p else 'T'

def get_age_range(age):
    if age < 21:
        return 1
    elif age < 41:
        return 2
    elif age < 61:
        return 3
    elif age < 81:
        return 4
    else:
        return 5

def get_tempo_range(tempo):
    if tempo < 108:
        return 1
    elif tempo < 120:
        return 2
    else:
        return 3

def generate_probability_map():
    for i, u in enumerate(users):
        for j, m in enumerate(music):
            key = str(get_age_range(u['age'])) + u['gender'] + str(get_tempo_range(m['tempo'])) + m['genre']
            if key not in probabilities:
                probabilities[key] = random.uniform(0,1)
            add = flip(probabilities[key])
            if add == 'H':
                preferences.append([u['id'], m['id']])

generate_probability_map()

with open('preferences.csv', 'w') as fp:
    a = csv.writer(fp, delimiter=',')
    a.writerows(preferences)
