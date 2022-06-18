###### OOMP FILE  ######

import OOMP

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "kicad")
newPart.addTag("oompColor", "kicad-footprints")
newPart.addTag("oompDesc", "Package_DIP")
newPart.addTag("oompIndex", "DIP-40_W15.24mm")

newPart.addTag("kicadDesc", "40-lead though-hole mounted DIP package, row spacing 15.24 mm (600 mils)")
newPart.addTag("kicadTags", "THT DIP DIL PDIP 2.54mm 15.24mm 600mil")
newPart.addTag("kicadAttr", "through_hole")
newPart.addTag("kicad3DModel", "${KICAD6_3DMODEL_DIR}/Package_DIP.3dshapes/DIP-40_W15.24mm.wrl")

OOMP.parts.append(newPart)