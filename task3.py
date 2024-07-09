import re

raw_numbers = ['80(97) 943 (22) 15', '0(97) 54333 15']

def normalize_phone(phone):
    res = re.sub(r'[\D]','', phone)
    if res.startswith('38'):
        res = '+' + res
    elif res.startswith('8'):
        res = '+3' + res
    elif res.startswith('0'):
        res = '+38' + res
    return res

def get_sanitized_numbers(numbers):
    sanitized_numbers = [normalize_phone(phone) for phone in numbers]
    print("Нормалізовані номери телефонів для SMS-розсилки:", sanitized_numbers )

get_sanitized_numbers(raw_numbers)
