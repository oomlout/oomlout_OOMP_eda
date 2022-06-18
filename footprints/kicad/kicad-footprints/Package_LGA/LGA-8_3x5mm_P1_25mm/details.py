###### OOMP FILE  ######

import OOMP

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "kicad")
newPart.addTag("oompColor", "kicad-footprints")
newPart.addTag("oompDesc", "Package_LGA")
newPart.addTag("oompIndex", "LGA-8_3x5mm_P1.25mm")

newPart.addTag("kicadDesc", "LGA-8")
newPart.addTag("kicadTags", "lga land grid array")
newPart.addTag("kicadAttr", "smd")
newPart.addTag("kicad3DModel", "${KICAD6_3DMODEL_DIR}/Package_LGA.3dshapes/LGA-8_3x5mm_P1.25mm.wrl")

OOMP.parts.append(newPart)