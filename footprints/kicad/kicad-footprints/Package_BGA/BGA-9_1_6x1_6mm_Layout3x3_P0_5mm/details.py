###### OOMP FILE  ######

import OOMP

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "kicad")
newPart.addTag("oompColor", "kicad-footprints")
newPart.addTag("oompDesc", "Package_BGA")
newPart.addTag("oompIndex", "BGA-9_1.6x1.6mm_Layout3x3_P0.5mm")

newPart.addTag("kicadDesc", "BGA-9, http://www.ti.com/lit/ds/symlink/bq27421-g1.pdf")
newPart.addTag("kicadTags", "BGA-9")
newPart.addTag("kicadAttr", "smd")
newPart.addTag("kicad3DModel", "${KICAD6_3DMODEL_DIR}/Package_BGA.3dshapes/BGA-9_1.6x1.6mm_Layout3x3_P0.5mm.wrl")

OOMP.parts.append(newPart)