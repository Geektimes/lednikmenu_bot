import json
import pprint

def convert_list_in_str(list):
    html_text = ''
    for x in list:
        myString = ''.join(str(x))
        html_text = html_text + myString + '\n'
    return html_text

with open('alcohol.json', 'r', encoding='utf-8') as f:
    korobka = json.load(f)
name = ''
y=0

name = list(korobka[0].keys())

for i in korobka:
    name = list(korobka[y].keys())
    if name[0] == "Белые вина (бокалы)":
        w_white = i[name[0]]

    y = y + 1
print(convert_list_in_str(w_white))