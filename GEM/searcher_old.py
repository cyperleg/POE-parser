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

prs_list = file_ex[2].split('\n')

LevelRequired = int(prs_list[2][6:])

prs_list = file_ex[4].split('\n')

Mods = []

print(prs_list[0])

for i in range(1,len(prs_list)-1):
    Mods.append(prs_list[i])

Corrupted = False

prs_list = file_ex[len(file_ex) - 2].split('\n')[1]

if prs_list == "Corrupted":
    Corrupted = True

print(GemName + '\n' + str(GemLevel) + '\n' + str(LevelRequired) + '\n' + str(Corrupted))
print(Mods)

#parse End

file = open('results.txt','w')
file_name = open('same_name.txt','w')
file_price = open('price.txt','w')

name_list = []

for i in range(len(temp)):
    if temp[i]['name'] == GemName:
        name_list.append(temp[i])
        file_name.write(str(temp[i]) + '\n')
        print(i)

if len(name_list) == 0:
    print("Incorrect gem name!")
elif len(name_list) == 1:
    file.write(str(name_list[0]) + '\n')
elif len(name_list) > 1:
    items = []
    t_Mods = []
    for i in range(len(name_list)):
        t_Mods.clear()
        for j in range(len(Mods)):
            t_Mods.append(Mods[j])
        counter = 0
        if name_list[i]['gemLevel'] == GemLevel:
            counter += 1
        if name_list[i]['levelRequired'] == LevelRequired:
            counter += 1
        try:
            if name_list[i]['corrupted'] == Corrupted:
                counter += 1
        except:
            counter += 0
        for j in range(len(name_list[i]['explicitModifiers'])):
            for k in range(len(t_Mods)):
                if name_list[i]['explicitModifiers'][j]['text'] == t_Mods[k]:
                    counter += 1
                    t_Mods.remove(t_Mods[k])
                    break
        items.append(counter)
        print("i = " + str(i) + " counter = " + str(counter))
        print(items)
    price_list = []
    if min(items)==max(items):
        file_price.write("0" + '\n')
    else:
        for i in range(len(items)):
            if items[i] == max(items):
                file.write(str(name_list[i]).replace(',','\n') + '\n')
                file.write('\n\n\n-------\n\n\n')
                price_list.append(name_list[i]['chaosValue'])
        price = 0
        for i in range(len(price_list)):
            price += price_list[i]
        price = round(price / len(price_list))
        file_price.write(str(price) + '\n')


"""
for i in range(len(temp)):
    try:
        if temp[i]['name'] == GemName and temp[i]['gemLevel'] == GemLevel and temp[i]['levelRequired'] == LevelRequired and temp[i]['corrupted'] == Corrupted:
            mods = temp[i]['explicitModifiers']
            counter = 0
            for j in range(len(mods)):
                if mods[j]['text'] == Mods[j]:
                    counter += 1
            if counter == len(mods):
                file.write(str(temp[i]) + '\n')
                print(i)
    except:
        i += 1
"""

file_price.close()
file_name.close()
file.close()

with open('data.txt', 'w') as f:
    f.write(str(data))

