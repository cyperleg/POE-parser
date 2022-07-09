import requests

data = requests.get("https://poe.ninja/api/data/itemoverview?league=Expedition&type=ClusterJewel").json()

temp = data['lines']

#parse Start

with open("parse.txt","r") as f:
    file_ex = f.read().split('--------')

prs_list = file_ex[2].split('\n')

JewLevel = int(prs_list[1][11:])

if JewLevel < 84 and JewLevel >= 75:
    JewLevel = 75
elif JewLevel >= 84:
    JewLevel = 84
elif JewLevel < 75 and JewLevel >= 68:
    JewLevel = 68
elif JewLevel < 60 and JewLevel > 1:
    JewLevel = 50
else:
    JewLevel = 1

prs_list = file_ex[3].split('\n')



P_variant = '-' + str(int(prs_list[1].split(" Passive Skills (enchant)")[0][5:])) + '-passives-'

JewName = str(prs_list[len(prs_list) - 2].split("Added Small Passive Skills grant: ")[1].split(" (enchant)")[0])

JewName = JewName.lower().replace('%','').replace(' ','-')

detid = JewName + P_variant + str(JewLevel)

print(detid)

#parse End

file_price = open('price.txt','w')

for i in range(len(temp)):
    if temp[i]['detailsId'] == detid:
        file_price.write(str(temp[i]['chaosValue']))
        break

file_price.close()

