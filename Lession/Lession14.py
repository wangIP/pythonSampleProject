#網路連線
#import urllib request
#下載特定網址資料
#處理json格式 
# json.load()
import urllib.request as request
import json
with request.urlopen() as response:
    data=response.read()
print(data)