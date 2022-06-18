###### OOMP FILE  ######

import OOMP

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "kicad")
newPart.addTag("oompColor", "kicad-footprints")
newPart.addTag("oompDesc", "Package_DIP")
newPart.addTag("oompIndex", "DIP-8_W10.16mm")

newPart.addTag("kicadDesc", "8-lead though-hole mounted DIP package, row spacing 10.16 mm (400 mils)")
newPart.addTag("kicadTags", "THT DIP DIL PDIP 2.54mm 10.16mm 400mil")
newPart.addTag("kicadAttr", "through_hole")
newPart.addTag("kicad3DModel", "${KICAD6_3DMODEL_DIR}/Package_DIP.3dshapes/DIP-8_W10.16mm.wrl")

OOMP.parts.append(newPart)