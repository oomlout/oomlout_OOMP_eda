###### OOMP FILE  ######

import OOMP

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "kicad")
newPart.addTag("oompColor", "kicad-footprints")
newPart.addTag("oompDesc", "Package_DIP")
newPart.addTag("oompIndex", "DIP-20_W8.89mm_SMDSocket_LongPads")

newPart.addTag("kicadDesc", "20-lead though-hole mounted DIP package, row spacing 8.89 mm (350 mils), SMDSocket, LongPads")
newPart.addTag("kicadTags", "THT DIP DIL PDIP 2.54mm 8.89mm 350mil SMDSocket LongPads")
newPart.addTag("kicadAttr", "smd")
newPart.addTag("kicad3DModel", "${KICAD6_3DMODEL_DIR}/Package_DIP.3dshapes/DIP-20_W8.89mm_SMDSocket.wrl")

OOMP.parts.append(newPart)