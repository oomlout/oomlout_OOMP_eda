###### OOMP FILE  ######

import OOMP

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "kicad")
newPart.addTag("oompColor", "kicad-footprints")
newPart.addTag("oompDesc", "Package_BGA")
newPart.addTag("oompIndex", "BGA-90_8.0x13.0mm_Layout2x3x15_P0.8mm")

newPart.addTag("kicadDesc", "BGA-90, http://www.issi.com/WW/pdf/42-45S32800J.pdf")
newPart.addTag("kicadTags", "BGA-90")
newPart.addTag("kicadAttr", "smd")
newPart.addTag("kicad3DModel", "${KICAD6_3DMODEL_DIR}/Package_BGA.3dshapes/BGA-90_8.0x13.0mm_Layout2x3x15_P0.8mm.wrl")

OOMP.parts.append(newPart)