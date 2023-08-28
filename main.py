
import csv
import re
with open("phonebook_raw.csv", encoding='UTF-8') as f:
    rows = csv.reader(f, delimiter=",")
    contacts_list = list(rows)

res1 = {}
for i in contacts_list:
    i = ','.join(i)
    pattern = re.compile(r'(^\w*) ?,?(\w*)? ?,?(\w*)?,{1,3}(\w*)?,{1,2}([^0-9,A-Z+]*)?,([^,A-Z]*),*([^\
    ]*)')
    sub_pattern = r"\1,\2,\3,\4,\5,\6,\7"
    res = pattern.sub(sub_pattern, i)

    phone = re.compile(r'\+?(7|8) ?\(?(\d{1,3})\)? ?-?(\d{2,3})-?(\d{2})-?(\d*) ?\(?(доб. \d*)?\)?')
    phone_pettern = r"+7(\2)-\3-\4-\5 \6"
    i = pattern.sub(sub_pattern, i)
    i = (phone.sub(phone_pettern, i).split(','))
    if i[0] not in res1:
        res1.update({i[0]: i})
    else:
        for j, x in enumerate(res1[i[0]]):
            if not x:
                res1[i[0]][j] = i[j]
data = []
for x, y in res1.items():
    y = [str_ for str_ in y if len(str_)]
    data.append(y)

with open("phonebook.csv", "w", encoding='UTF-8') as f:
    datawriter = csv.writer(f, delimiter=',')
    datawriter.writerows(data)



