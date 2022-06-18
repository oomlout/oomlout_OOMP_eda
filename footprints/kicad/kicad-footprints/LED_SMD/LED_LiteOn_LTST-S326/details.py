###### OOMP FILE  ######

import OOMP

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "kicad")
newPart.addTag("oompColor", "kicad-footprints")
newPart.addTag("oompDesc", "LED_SMD")
newPart.addTag("oompIndex", "LED_LiteOn_LTST-S326")

newPart.addTag("kicadDesc", "http://optoelectronics.liteon.com/upload/download/DS22-2000-287/LTST-S326KGJRKT.PDF")
newPart.addTag("kicadTags", "LED SMD right angle  CCA")
newPart.addTag("kicadAttr", "smd")
newPart.addTag("kicad3DModel", "${KICAD6_3DMODEL_DIR}/LED_SMD.3dshapes/LED_LiteOn_LTST-S326.wrl")

OOMP.parts.append(newPart)