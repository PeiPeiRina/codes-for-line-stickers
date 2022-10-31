import os
import numpy as np
lowerpath="C:/Users/dexck/Desktop/stamp220213/2022/PNG/Wendy/"


lowerfilelist=os.listdir(lowerpath)
lowerfilearr= np.array(lowerfilelist) 

i = 0
while i < lowerfilearr.size:

    oldname=lowerpath+ os.sep + lowerfilearr[i]

    if "Thumbs.db" in str(oldname):
        newname = oldname
    elif 8 < i <lowerfilearr.size-2:
        newname=lowerpath + os.sep +str(i+1)+".PNG"
    elif i<9:
        newname=lowerpath + os.sep +"0"+str(i+1)+".PNG"
    elif i == lowerfilearr.size-2:
        newname=lowerpath + os.sep +"main"+".PNG"
    else: 
        newname=lowerpath + os.sep +"tab"+".PNG"
    os.rename(oldname,newname)

    i+=1