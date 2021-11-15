import argparse
import json
import re
import autopep8
from tqdm import tqdm




class Validator:

    def __init__(self):
        pass

    def control_email(email) -> bool:
        if type(email) != str:
            return False
        pattern = '^[^\s@]+@([^\s@.,]+\.)+[^\s@.,]{2,}$'
        if re.match(pattern, email):
            return True
        return False

    def control_weight(weight: str) -> bool:
        pattern = '\d{2,3}'
        if re.match(pattern, str(weight)) is not None:
            if (int(weight) < 150 and int(weight) > 40):
                return True
        return False

    def control_inn(inn: str) -> bool:
        if len(inn) == 11:
            return True
        return False

    def control_passport(passport_number: int) -> bool:
        if len(str(passport_number)) == 6:
            return True
        return False

    def control_address(address) -> bool:
        pattern = '[а-яА-Я \-.0-9]{1,}[а-яА-Я0-9]{1,}'
        if type(address) != str:
            return False
        if re.match(pattern, address):
            return True
        return False

    def control_experience(number) -> bool:
        if type(number) == int:
            if (number < 80 and number > 0):
                return True
        return False

    def control_string(string) -> str:
        if type(string) != str:
            return False
        return True

parser = argparse.ArgumentParser()
parser.add_argument('-input', type = str, help='Get path file input', dest='input')
parser.add_argument('-output', type = str, help='Get path file output', dest='output')
args = parser.parse_args()
data = json.load(open(args.input, encoding='windows-1251'))

true_data = list()
email = 0
weight = 0
inn = 0
passport_number = 0
work_experience = 0
university = 0
political_view = 0
worldview = 0
address = 0
with tqdm(total=len(data)) as progressbar:
    for person in data:
        temp = True
        if not Validator.control_email(person['email']):
            email += 1
            temp = False
        if not Validator.control_weight(person['weight']):
            weight += 1
            temp = False
        if not Validator.control_inn(person['inn']):
            inn += 1
            temp = False
        if not Validator.control_passport(person['passport_number']):
            passport_number += 1
            temp = False
        if not Validator.control_string(person['university']):
            university += 1
            temp = False
        if not Validator.control_experience(person['work_experience']):
            work_experience += 1
            temp = False
        if not Validator.control_string(person['political_views']):
            political_view += 1
            temp = False
        if not Validator.control_string(person['worldview']):
            worldview += 1
            temp = False
        if not Validator.control_address(person["address"]):
            address += 1
            temp = False
        if temp:
            true_data.append(person)
        progressbar.update(1)

out = open(args.output, 'w', encoding='utf-8')
new_data = json.dumps(true_data, ensure_ascii=False, indent=4)
out.write(new_data)
out.close()

print(f'Число валидных записей: {len(true_data)}')
print(f'Число невалидных записей: {len(data) - len(true_data)}')
print(f'Число невалидных адресов электронной почты:  {email}')
print(f'Число невалидных маcc: {weight}')
print(f'Число невалидных номеров: {inn}')
print(f'Число невалидных паспортных номеров: {passport_number}')
print(f'Число невалидных университетов: {university}')
print(f'Число невалидных рабочих стажей: {work_experience}')
print(f'Число невалидных политических взглядов: {political_view}')
print(f'Число невалидных мировоззрений: {worldview}')
print(f'Число невалидных адрессов: {address}')

#python.exe main.py - input C:\\test\\input.txt - output C:\\test\\output.txt









