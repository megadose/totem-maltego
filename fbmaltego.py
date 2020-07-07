from MaltegoTransform import *
import json,requests,base64
from facebook_totem import *

id=str(sys.argv).split("id=")[1].split("#category")[0]

trx = MaltegoTransform()
for ad in getAdsFromId(id):
    poost = trx.addEntity("megadose.FacebookAdsPosts", ad["adArchiveID"])
    jsoovalue=str(json.dumps(ad))
    b64value=str(base64.b64encode(jsoovalue.encode('ascii')).decode("utf-8"))
    poost.addProperty(fieldName="jsonInfo",value=b64value)

print(trx.returnOutput())
