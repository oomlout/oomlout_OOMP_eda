###### OOMP FILE  ######

import OOMP

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "kicad")
newPart.addTag("oompColor", "kicad-footprints")
newPart.addTag("oompDesc", "Package_TO_SOT_SMD")
newPart.addTag("oompIndex", "SOT-223-8")

newPart.addTag("kicadDesc", "module CMS SOT223 8 pins, https://www.diodes.com/assets/Datasheets/ZXSBMR16PT8.pdf")
newPart.addTag("kicadTags", "CMS SOT")
newPart.addTag("kicadAttr", "smd")
newPart.addTag("kicad3DModel", "${KICAD6_3DMODEL_DIR}/Package_TO_SOT_SMD.3dshapes/SOT-223-8.wrl")

OOMP.parts.append(newPart)