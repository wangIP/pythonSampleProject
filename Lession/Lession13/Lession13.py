#開啟檔案 讀取寫入 關閉檔案
#檔案物件= open (檔案路徑,mode= 開啟模式)

#讀取檔案
#檔案物件.read()  讀取全部文字
#一行一行讀的話用for
#for 變數 in 檔案物件:
  #從檔案依序讀取每行文字到變數中

#讀取JSON格式
#import json 
#讀取到的資料=json.load(檔案物件)
#寫入json格式
#json.dump(要寫入的資料, 檔案物件)

#寫入檔案 儲存檔案
#檔案物件.write()
#/n換行

#關閉檔案
#檔案物件.close()

#with open(檔案路徑,mode=開啟模式) as 檔案物件:
#  讀取或寫入檔案的程式

#寫入
# file = open("test.txt",mode="w",encoding="UTF-8")
# file.write("こんにちは")
# file.close()
# with open("test.txt",mode="w",encoding="UTF-8")as file:
#   file.write("中文\n棒")

# list=[]
# with open("test.txt",mode="r",encoding="UTF-8")as file:
#   for str in file:
#     list.append(str)
# print(list)

#使用json 讀取 複寫
import json
with open("config.json",mode="r")as file:
  data=json.load(file)
print("name",data["name"])
print("age",data["age"])