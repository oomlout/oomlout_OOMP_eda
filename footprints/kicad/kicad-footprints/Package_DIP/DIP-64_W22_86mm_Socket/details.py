###### OOMP FILE  ######

import OOMP

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "kicad")
newPart.addTag("oompColor", "kicad-footprints")
newPart.addTag("oompDesc", "Package_DIP")
newPart.addTag("oompIndex", "DIP-64_W22.86mm_Socket")

newPart.addTag("kicadDesc", "64-lead though-hole mounted DIP package, row spacing 22.86 mm (900 mils), Socket")
newPart.addTag("kicadTags", "THT DIP DIL PDIP 2.54mm 22.86mm 900mil Socket")
newPart.addTag("kicadAttr", "through_hole")
newPart.addTag("kicad3DModel", "${KICAD6_3DMODEL_DIR}/Package_DIP.3dshapes/DIP-64_W22.86mm_Socket.wrl")

OOMP.parts.append(newPart)