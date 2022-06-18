###### OOMP FILE  ######

import OOMP

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "kicad")
newPart.addTag("oompColor", "kicad-footprints")
newPart.addTag("oompDesc", "RF_WiFi")
newPart.addTag("oompIndex", "USR-C322")

newPart.addTag("kicadDesc", "https://www.usriot.com/download/WIFI/USR-C322-Hardware-Manual_V1.2.01.pdf")
newPart.addTag("kicadTags", "WiFi IEEE802.11 b/g/n")
newPart.addTag("kicadAttr", "smd")
newPart.addTag("kicad3DModel", "${KICAD6_3DMODEL_DIR}/RF_WiFi.3dshapes/USR-C322.wrl")

OOMP.parts.append(newPart)