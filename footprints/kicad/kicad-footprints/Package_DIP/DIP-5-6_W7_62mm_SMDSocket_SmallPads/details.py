###### OOMP FILE  ######

import OOMP

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "kicad")
newPart.addTag("oompColor", "kicad-footprints")
newPart.addTag("oompDesc", "Package_DIP")
newPart.addTag("oompIndex", "DIP-5-6_W7.62mm_SMDSocket_SmallPads")

newPart.addTag("kicadDesc", "5-lead though-hole mounted DIP package, row spacing 7.62 mm (300 mils), SMDSocket, SmallPads")
newPart.addTag("kicadTags", "THT DIP DIL PDIP 2.54mm 7.62mm 300mil SMDSocket SmallPads")
newPart.addTag("kicadAttr", "smd")
newPart.addTag("kicad3DModel", "${KICAD6_3DMODEL_DIR}/Package_DIP.3dshapes/DIP-5-6_W7.62mm_SMDSocket.wrl")

OOMP.parts.append(newPart)