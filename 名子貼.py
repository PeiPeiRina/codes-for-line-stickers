#! /usr/bin/env python3

from psd_tools import PSDImage
import os
import numpy as np

#存放psd的資料夾
path = 'C:/Users/dexck/Desktop/stamp220213/2022/名子貼6-7月/名子5/'

#png存檔位置 --> pngsave
pngpath = 'C:/Users/dexck/Desktop/stamp220213/2022/名子貼6-7月/PNG/'
def pngfilepath(d):
    filelist=os.listdir(pngpath)
    filearr= np.array(filelist)
    pngsave = pngpath+filearr[d]+'/'
    return pngsave


filelist=os.listdir(path)
filearr= np.array(filelist) 
lenfile = len(filearr)

#psd檔全部名子不顯示
def cancelvisi():
    for a in range(lenfile):
        #打開psd檔
        psdfile = PSDImage.open(path+filearr[a])
        #單個圖層處理
        layerlen = len(psdfile._layers)
        #所有"? 的複製"的圖層改為不顯示
        for b in range(layerlen):
            lyname = psdfile[b].name
            if ' 的複製' in lyname and len(lyname) <= 6:
                if psdfile[b].visible == True:
                    psdfile[b].visible = False
        #儲存psd檔
        psdfile.save(path+filearr[a])

#呼叫名子不顯示函數，需要時開啟
cancelvisi()

#依psd檔案數量逐一處裡
for a in range(0,42):

    #打開單個psd檔
    psd = PSDImage.open(path+filearr[a])
    #psd檔的圖層數
    layerlen = len(psd._layers)

    c = 8#需修改部分
    #從"? 的複製"開始，到最後一個"? 的複製"圖層，逐一打開顯示、另存png檔、關閉顯示
    d = 6#需修改部分
    #png存檔資料夾的索引，從第?個[?]開始，逐一遞增

    #圖層逐一處理
    for b in range(layerlen):
        lyname = psd[b].name

        if lyname == str(c)+' 的複製':
            #找到要的圖層，設為顯示
            psd[b].visible = True

            #取得當前psd檔的名稱前兩位數
            psdname = filearr[a]
            psdname = psdname[0:-4]

            #呼叫取得存檔位置函數
            pngsave = pngfilepath(d)

            #取得完整存放位置
            pngadrass = pngsave+psdname+".png"

            #呼叫取得存檔位置函數
            pngsave = pngfilepath(d)

            #存檔            
            image = psd.compose(force=True)
            image.save(pngadrass)

            #關閉顯示
            psd[b].visible = False
            #c和d參數+1
            c += 1
            d += 1
            
            if c == 10:#需修改部分
            #如果c參數超過需要的值，跳出迴圈
                break




