import urllib.request as req
import random
import time
import json

with open("linenew.json", mode="r") as file:
    dict=json.load(file)

def linecreator(address, time):
    while time > 0:
        request = req.Request(address, headers={
            "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36"
        })
        req.urlopen(request)
        time-=1

tdictlist = dict["1"]
mdictlist = dict["2"]

trangelist = list(range(40, 60, 1)) #連結網頁40到60次
mrangelist = list(range(30, 60, 1)) #停頓30到60分鐘

for i in tdictlist:
    if i in trangelist:
        trangelist.remove(i)

for j in mdictlist:
    if j in mrangelist:
        mrangelist.remove(j)


exeround = 0 #↓共重複5回
while exeround < 5:

    ts = random.choice(trangelist)

    linecreator("http://asilentghost.blogspot.com/2012/07/blog-post_31.html", ts)

    trangelist.remove(ts)

    tdictlist[exeround] = ts 

    ms = random.choice(mrangelist)
    mrangelist.remove(ms)

    mdictlist[exeround] = ms 
    
    sec = ms*60
    time.sleep(sec)

    exeround += 1

dict["1"] = tdictlist
dict["2"] = mdictlist

with open("linenew.json", mode="w") as file:
    json.dump(dict, file)

print("end")
