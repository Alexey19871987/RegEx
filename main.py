import csv
from pprint import pprint
import re
pattern = r'([А-ЯЁ][а-яё]+)[\s,]*([А-ЯЁ][а-яё]+)[\s,]*([А-ЯЁ][а-яё]+)?[\s,]*([А-Я]\w+)?' \
          r'[,]([^A-Za-z0-9+,]+)?[,]+(\+7|8)?[\s\(]*(\d{3})?[\)\s-]*(\d{3})?[-]*(\d{2})?[-]*' \
          r'(\d{2})?[ (]*([доб.]+ \d*[)]?)?[,]?([A-Za-z0-9.@]+)?'
pattern_sub = r'\1,\2,\3,\4,\5,+7 (\7)\8-\9-\10 \11,\12'
with open("phonebook_raw.csv", encoding='utf=8') as f:
    rows = csv.reader(f, delimiter=",")
    contacts_list = list(rows)
contacts_list_new = []
contacts_list_temp = []
for part_list in contacts_list:
    part_list = ','.join(part_list)
    new_list = re.sub(pattern, pattern_sub, part_list).split(',')
    contacts_list_new.append(new_list)
    contacts_list_temp.append(new_list)
for part_list_new in contacts_list_new:
    for part_list_temp in contacts_list_temp:
        if part_list_new[0] == part_list_temp[0] and part_list_new[1] == part_list_temp[1] and part_list_new.count('') > part_list_temp.count(''):
            contacts_list_new.remove(part_list_new)
with open("phonebook.csv", "w", encoding='utf=8') as f:
    datawriter = csv.writer(f, delimiter=',')
    datawriter.writerows(contacts_list_new)
