###### OOMP FILE  ######

import OOMP

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "kicad")
newPart.addTag("oompColor", "kicad-footprints")
newPart.addTag("oompDesc", "LED_THT")
newPart.addTag("oompIndex", "LED_D1.8mm_W3.3mm_H2.4mm")

newPart.addTag("kicadDesc", "LED, Round,  Rectangular size 3.3x2.4mm^2 diameter 1.8mm, 2 pins")
newPart.addTag("kicadTags", "LED Round  Rectangular size 3.3x2.4mm^2 diameter 1.8mm 2 pins")
newPart.addTag("kicadAttr", "through_hole")
newPart.addTag("kicad3DModel", "${KICAD6_3DMODEL_DIR}/LED_THT.3dshapes/LED_D1.8mm_W3.3mm_H2.4mm.wrl")

OOMP.parts.append(newPart)