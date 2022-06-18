###### OOMP FILE  ######

import OOMP

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "kicad")
newPart.addTag("oompColor", "kicad-footprints")
newPart.addTag("oompDesc", "Package_BGA")
newPart.addTag("oompIndex", "BGA-25_6.35x6.35mm_Layout5x5_P1.27mm")

newPart.addTag("kicadDesc", "BGA-25, http://cds.linear.com/docs/en/datasheet/4624fc.pdf")
newPart.addTag("kicadTags", "BGA-25 uModule")
newPart.addTag("kicadAttr", "smd")
newPart.addTag("kicad3DModel", "${KICAD6_3DMODEL_DIR}/Package_BGA.3dshapes/BGA-25_6.35x6.35mm_Layout5x5_P1.27mm.wrl")

OOMP.parts.append(newPart)