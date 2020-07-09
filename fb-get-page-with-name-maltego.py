from MaltegoTransform import *
from facebook_totem import *
id=sys.argv[1]

trx = MaltegoTransform()

for page in getFacebookPageFromName(id):
    PageFb = trx.addEntity("megadose.facebookpage", page["name"].replace("&","&amp;"))
    PageFb.addProperty(fieldName="id",value=str(page["id"]))
    PageFb.addProperty(fieldName="category",value=str(page["category"].replace("&","&amp;")))
    PageFb.addProperty(fieldName="likes",value=str(page["likes"]))
    PageFb.addProperty(fieldName="verification",value=str(page["verification"]))
    PageFb.addProperty(fieldName="igUsername",value=str(page["igUsername"]))
    PageFb.addProperty(fieldName="igFollowers",value=str(page["igFollowers"]))
    PageFb.addProperty(fieldName="igVerification",value=str(page["igVerification"]))
    PageFb.addProperty(fieldName="pageIsDeleted",value=str(page["pageIsDeleted"]))
    PageFb.setIconURL(page["imageURI"].replace("&","&amp;"))

print(trx.returnOutput())
