import requests

data = requests.get("https://poe.ninja/api/data/itemoverview?league=Expedition&type=SkillGem").json()


temp = data['lines']

#parse Start

with open("examples.txt","r") as f:
    file_ex = f.read().split('--------')

prs_list = file_ex[0].split('\n')

GemName = prs_list[len(prs_list) - 2]

prs_list = file_ex[1].split('\n')

GemLevel = int(prs_list[2].split(" (Max)")[0][6:])

if GemLevel < 20:
    GemLevel = 1

GemQuality = 0

if prs_list[len(prs_list)-2][:7] == "Quality":
    GemQuality = int(prs_list[len(prs_list)-2].split(" (augmented)")[0].split("Quality: +")[1].split("%")[0])
    if GemQuality > 20:
        GemQuality = 23
    elif GemQuality >= 10:
        GemQuality = 20
    elif GemQuality < 10:
        GemQuality = 0
        

Corrupted = False

prs_list = file_ex[len(file_ex) - 2].split('\n')[1]
prs_list_ex = file_ex[len(file_ex) - 1].split('\n')[1]

if prs_list == "Corrupted" or prs_list_ex == "Corrupted":
    Corrupted = True

#parse End

file_price = open('price.txt','w')
file_name = open('same_name.txt','w')

var = str(GemLevel)
if GemQuality != 0:
    var = var + '/' + str(GemQuality)
if Corrupted:
    var = var + 'c'

print(var)

check = True

for i in range(len(temp)):
    if temp[i]['name'] == GemName:
        file_name.write(str(temp[i]) + '\n')

for i in range(len(temp)):
    if temp[i]['name'] == GemName and temp[i]['variant'] == var:
        file_price.write(str(temp[i]['chaosValue']))
        check = False
        break
if check:
    file_price.write('0')

file_price.close()
file_name.close()


