###### OOMP FILE  ######

import OOMP

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "kicad")
newPart.addTag("oompColor", "kicad-footprints")
newPart.addTag("oompDesc", "Package_DIP")
newPart.addTag("oompIndex", "DIP-42_W16.51mm_SMDSocket_LongPads")

newPart.addTag("kicadDesc", "42-lead though-hole mounted DIP package, row spacing 16.51 mm (650 mils), SMDSocket, LongPads")
newPart.addTag("kicadTags", "THT DIP DIL PDIP 2.54mm 16.51mm 650mil SMDSocket LongPads")
newPart.addTag("kicadAttr", "smd")
newPart.addTag("kicad3DModel", "${KICAD6_3DMODEL_DIR}/Package_DIP.3dshapes/DIP-42_W16.51mm_SMDSocket.wrl")

OOMP.parts.append(newPart)