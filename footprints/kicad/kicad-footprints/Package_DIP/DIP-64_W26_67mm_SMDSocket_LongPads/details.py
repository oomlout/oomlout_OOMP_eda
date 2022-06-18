###### OOMP FILE  ######

import OOMP

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "kicad")
newPart.addTag("oompColor", "kicad-footprints")
newPart.addTag("oompDesc", "Package_DIP")
newPart.addTag("oompIndex", "DIP-64_W26.67mm_SMDSocket_LongPads")

newPart.addTag("kicadDesc", "64-lead though-hole mounted DIP package, row spacing 26.67 mm (1050 mils), SMDSocket, LongPads")
newPart.addTag("kicadTags", "THT DIP DIL PDIP 2.54mm 26.669999999999998mm 1050mil SMDSocket LongPads")
newPart.addTag("kicadAttr", "smd")
newPart.addTag("kicad3DModel", "${KICAD6_3DMODEL_DIR}/Package_DIP.3dshapes/DIP-64_W26.67mm_SMDSocket.wrl")

OOMP.parts.append(newPart)