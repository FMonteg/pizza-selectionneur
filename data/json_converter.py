import json
import os


project_prefix = "pza_"

file_name = "compositions"

file_path = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'texte_brut.txt')
with open(file_path, encoding='utf-8') as f:
    texte_brut = f.readlines()
print(texte_brut)



table = {}
while len(texte_brut)>0:
    temp = texte_brut[0][:-1].split(" : ")
    index = temp[0]
    ingredients = temp[1].split(', ')
    ingred = " ".join([ing.lower() for ing in ingredients])
    table[index] = ingred
    del texte_brut[0]

print(table)


file_path = os.path.join(os.path.abspath(os.path.dirname(__file__)), project_prefix+file_name+'.json')

with open(file_path, 'w') as json_file:
    json.dump(table, json_file, indent=4)
    pass



file_name = "ingredients"

ingredients = {}
for k in table.keys():
    for i in table[k].split(' '):
        ingredients[i] = ingredients.get(i, []) + [k]

for k in ingredients.keys():
    print(k)
    print(ingredients[k])



file_path = os.path.join(os.path.abspath(os.path.dirname(__file__)), project_prefix+file_name+'.json')

with open(file_path, 'w') as json_file:
    json.dump(ingredients, json_file, indent=4)
    pass




