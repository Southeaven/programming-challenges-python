import random

with open('male_names.txt') as file:
    male_names = [n.strip() for n in file]

with open('female_names.txt') as file:
    female_names = [n.strip() for n in file]

with open('last_names.txt') as file:
    last_names = [n.strip() for n in file]

def get_gender():
    if random.randint(0, 1) == 0:
        return 'Male'
    else:
        return 'Female'

def get_first_name(gender):
    if gender == 'Male':
        return random.choice(male_names).capitalize()
    else:
        return random.choice(female_names).capitalize()

def get_last_name():
    return random.choice(last_names).capitalize()

def get_full_name(first_name, last_name):
    return first_name + ' ' + last_name

if __name__ == '__main__':
    print(get_full_name(get_first_name(get_gender()), get_last_name()))
