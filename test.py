from pystocknow import sndata
import json

SNClient = sndata.SNClient

#
# get API key from https://stocknow.xyz
# after you signin, run https://stocknow.xyz/v1/apikey in browser, you will get an apikey
# To get an apikey for programming purpose, please follow instruction ...
#
snclient = SNClient(apikey="")
data = snclient.get_news()
print(json.dumps(data, indent=2))
