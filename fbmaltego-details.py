from MaltegoTransform import *
import json,requests,base64,random,string
id=sys.argv[2].split("jsonInfo=")[1]
global trx
trx = MaltegoTransform()
import requests,json
data=json.loads(base64.b64decode(id).decode("utf-8"))

def addIfNotNone(entity,value,toadd):
    if str(value) !="None":
        if str(value)!="":
            trx.addEntity(entity,toadd+str(value).replace("<","&lt;"))

addIfNotNone("megadose.versionsAdNumber",str(data["collationCount"]),"")
addIfNotNone("megadose.Impressions",str(data["impressions"]),"")
addIfNotNone("megadose.Estimatereach",str(data["reachEstimate"]),"")
addIfNotNone("megadose.Countreport",str(data["reportCount"]),"")

addIfNotNone("megadose.Price",str(data["spend"]),"")
for platform in data["publisherPlatform"]:
    addIfNotNone("megadose.Platformpublisher",str(platform),"")

info = data["snapshot"]

addIfNotNone("megadose.Buyby",str(info["byline"]),"")
addIfNotNone("megadose.captionFb",str(info["caption"]),"")
addIfNotNone("megadose.display_format",str(info["display_format"]),"")
if info["title"]!=None:
    if "{{product.name}}" not in info["title"]:
        addIfNotNone("megadose.title",str(info["title"]),"")
addIfNotNone("megadose.link_url",str(info["link_url"]),"")
for video in info["videos"]:
    trx.addEntity("megadose.Attachment", video["video_sd_url"].replace("&","&amp;")).setIconURL(video["video_preview_image_url"].replace("&","&amp;"))

for images in info["images"]:
    trx.addEntity("megadose.Attachment", images["original_image_url"].replace("&","&amp;")).setIconURL(images["original_image_url"].replace("&","&amp;"))


additional_info=info["additional_info"]
if additional_info!=None:
    addIfNotNone("maltego.Person",additional_info["treasurer_name"],"treasurer_name : ")
    addIfNotNone("maltego.Person",str(additional_info["director_name"]), "director_name : ")
    addIfNotNone("maltego.Phrase",str(additional_info["point_of_contact"]),"point_of_contact : ")
    addIfNotNone("maltego.Phrase",str(additional_info["committee_id"]),"committee_id : ")

    addIfNotNone("maltego.PhoneNumber", str(additional_info["phone_number"]),"")
    addIfNotNone("maltego.EmailAddress", str(additional_info["email"]),"")
    addIfNotNone("maltego.Website", str(additional_info["website"]),"")
    addIfNotNone("maltego.Location", str(str(additional_info["street_address_1"])+" , "+str(additional_info["city"])+" , "+str(additional_info["zipcode"])).replace("/>",""),"")

print(trx.returnOutput())
