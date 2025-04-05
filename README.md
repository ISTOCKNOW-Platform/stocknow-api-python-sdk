# StockNow data &amp; insights API Client Library for Python
## Install package
```
pip3 install pystocknow
```

## Sample code of access StockNow platform provided data and insights
```
from pystocknow import sndata
import json

SNClient = sndata.SNClient

snclient = SNClient(apikey="eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1aWQiOiIwMDdRIiwiY3JlYXRlZEF0IjoiMjAyNS0wMy0yMFQwNDozMjowMi4yMjVaIiwiaWF0IjoxNzQyNDQ1MTIyLCJleHAiOjE3NDMwNDk5MjJ9.LEyRrT_CNjA8A6rpoiW5H7e3LwxXuvu3I9aOHMGME1U")
data = snclient.get_news()
print(json.dumps(data, indent=2))
```