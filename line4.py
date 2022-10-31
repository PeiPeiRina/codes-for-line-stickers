import urllib.request as req
import random
import json
with open("line4.json", mode="r") as file:
    data=json.load(file)

data_keys = list(data.keys())

def linecreator(address, time):
    while time > 0:
        request = req.Request(address, headers={
            "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.117 Safari/537.36"
        })
        req.urlopen(request)
        time-=1

grades=[
    0,0,0,0,0,
    0,0,0,0,0,
    0,0,0,0,0,
    0,0,0,0,0,
    0,0,0,0,0,
    0,0,0,0,0,]

def differ(datanum,listnum,th):
    print(listnum)
    while 1:
        if th==5:
            number = random.sample(range(50,60),1)
        elif th== 4:
            number = random.sample(range(40,50),1)
        elif th== 3:
            number = random.sample(range(30,40),1)
        elif th== 2:
            number = random.sample(range(20,30),1)
        elif th== 1:
            number = random.sample(range(10,20),1)

        num = int(number[0])
        
        if num in grades:
            continue

        if datanum in data_keys:
            if num == data[datanum]:
                continue
        break

    listnum-=1
    grades[listnum] = num
    data[datanum] = num
    with open("line4.json", mode="w") as file:
        json.dump(data, file)
    return num


n1 = differ("n1",1,4)
linecreator("https://line.me/S/sticker/20643350", n1)#玲沛33

n2 = differ("n2",2,2)
linecreator("https://line.me/S/sticker/18619093", n2)

n3 = differ("n3",3,2)
linecreator("https://line.me/S/sticker/19809277", n3)#天使43

n4 = differ("n4",4,2)
linecreator("https://line.me/S/sticker/18018759", n4)

n5 = differ("n5",5,2)
linecreator("https://line.me/S/sticker/19454342", n5)#布布12

n6 = differ("n6",6,5)
linecreator("https://store.line.me/stickershop/product/26715/zh-Hant", n6)

n7 = differ("n7",7,3)
linecreator("https://line.me/S/sticker/19981949", n7)#玲沛古裝

n8 = differ("n8",8,4)
linecreator("https://line.me/S/sticker/20384239", n8)#大天使

n9 = differ("n9",9,5)
linecreator("https://line.me/S/sticker/20566827", n9)#柳丁19

n10 = differ("n10",10,2)
linecreator("https://line.me/S/sticker/17700235", n10)

n11 = differ("n11",11,3)
linecreator("https://line.me/S/sticker/20211927", n11)#兔子4

n12 = differ("n12",12,1)
linecreator("https://line.me/S/sticker/17499466", n12)

n13 = differ("n13",13,1)
linecreator("https://line.me/S/sticker/19474032", n13)#柳丁職

n14 = differ("n14",14,5)
linecreator("https://line.me/S/sticker/20522737", n14)#棉球動物

n15 = differ("n15",15,2)
linecreator("https://line.me/S/sticker/17631521", n15)   

n16 = differ("n16",16,2)
linecreator("https://line.me/S/sticker/20015737", n16)#天使動

n17 = differ("n17",17,2)
linecreator("https://line.me/S/sticker/19554369", n17)#蘇打10

n18 = differ("n18",18,4)
linecreator("https://line.me/S/sticker/20438443", n18)#虎保4

n19 = differ("n19",19,2)
linecreator("https://line.me/S/sticker/19893584", n19)#亞瑟

n20 = differ("n20",20,1)
linecreator("https://line.me/S/sticker/19277810", n20)#虎寶3

n21 = differ("n21",21,2)
linecreator("https://line.me/S/sticker/19648238", n21)#玲沛31

n22 = differ("n22",22,5)
linecreator("https://line.me/S/sticker/14482220", n22)#玲沛

n23 = differ("n23",23,4)
linecreator("https://line.me/S/sticker/15701905", n23)#玲沛花


print("完成")


