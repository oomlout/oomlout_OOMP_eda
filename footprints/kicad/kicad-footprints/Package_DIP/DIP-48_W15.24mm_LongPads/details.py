###### OOMP FILE  ######

import OOMP

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "kicad")
newPart.addTag("oompColor", "kicad-footprints")
newPart.addTag("oompDesc", "Package_DIP")
newPart.addTag("oompIndex", "DIP-48_W15.24mm_LongPads")
newPart.addTag("oompName", "kicad-footprints/Package_DIP/DIP-48_W15.24mm_LongPads")

newPart.addTag("kicadDesc", "48-lead though-hole mounted DIP package, row spacing 15.24 mm (600 mils), LongPads")
newPart.addTag("kicadTags", "THT DIP DIL PDIP 2.54mm 15.24mm 600mil LongPads")
newPart.addTag("kicadAttr", "through_hole")
newPart.addTag("kicad3DModel", "${KICAD6_3DMODEL_DIR}/Package_DIP.3dshapes/DIP-48_W15.24mm.wrl")

OOMP.parts.append(newPart)