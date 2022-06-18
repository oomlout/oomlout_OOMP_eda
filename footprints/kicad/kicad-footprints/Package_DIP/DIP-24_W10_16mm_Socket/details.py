###### OOMP FILE  ######

import OOMP

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "kicad")
newPart.addTag("oompColor", "kicad-footprints")
newPart.addTag("oompDesc", "Package_DIP")
newPart.addTag("oompIndex", "DIP-24_W10.16mm_Socket")

newPart.addTag("kicadDesc", "24-lead though-hole mounted DIP package, row spacing 10.16 mm (400 mils), Socket")
newPart.addTag("kicadTags", "THT DIP DIL PDIP 2.54mm 10.16mm 400mil Socket")
newPart.addTag("kicadAttr", "through_hole")
newPart.addTag("kicad3DModel", "${KICAD6_3DMODEL_DIR}/Package_DIP.3dshapes/DIP-24_W10.16mm_Socket.wrl")

OOMP.parts.append(newPart)