###### OOMP FILE  ######

import OOMP

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "kicad")
newPart.addTag("oompColor", "kicad-footprints")
newPart.addTag("oompDesc", "Package_DIP")
newPart.addTag("oompIndex", "DIP-22_W7.62mm")
newPart.addTag("oompName", "kicad-footprints/Package_DIP/DIP-22_W7.62mm")

newPart.addTag("kicadDesc", "22-lead though-hole mounted DIP package, row spacing 7.62 mm (300 mils)")
newPart.addTag("kicadTags", "THT DIP DIL PDIP 2.54mm 7.62mm 300mil")
newPart.addTag("kicadAttr", "through_hole")
newPart.addTag("kicad3DModel", "${KICAD6_3DMODEL_DIR}/Package_DIP.3dshapes/DIP-22_W7.62mm.wrl")

OOMP.parts.append(newPart)