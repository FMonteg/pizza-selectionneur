import json
import os


project_prefix = "pnj_"

file_name = "qualites"

file_path = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'texte_brut.txt')
with open(file_path, encoding='utf-8') as f:
    texte_brut = f.readlines()
print(texte_brut)



table = {}
index = True
while len(texte_brut)>0:
    if index:
        id = int(texte_brut[0])
        index = False
    else:
        value = texte_brut[0][:-1]
        index = True
        table[id] = value
    del texte_brut[0]

print(table)

file_path = os.path.join(os.path.abspath(os.path.dirname(__file__)), project_prefix+file_name+'.json')

with open(file_path, 'w') as json_file:
    json.dump(table, json_file, indent=4)
    pass






### Obsolète : double table




# table_1 = {}
# table_2 = {}
# index = True
# Odd = True
# while len(texte_brut)>0:
#     if index:
#         id = int(texte_brut[0])
#         index = False
#     else:
#         value = texte_brut[0][:-1]
#         index = True
#         if Odd:
#             table_1[id] = value
#             Odd = False
#         else:
#             table_2[id] = value
#             Odd = True
#     del texte_brut[0]

# print(table_1)
# print(table_2)

# keys = [(k1, k2) for k1 in table_1.keys() for k2 in table_2.keys()]
# table = {}
# for k in keys:
#     table[str(k[0]) + ' ' + str(k[1])] = table_1[k[0]] + ' ' + table_2[k[1]]