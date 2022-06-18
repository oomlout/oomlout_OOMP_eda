###### OOMP FILE  ######

import OOMP

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "kicad")
newPart.addTag("oompColor", "kicad-footprints")
newPart.addTag("oompDesc", "Package_SO")
newPart.addTag("oompIndex", "VSSOP-8_3.0x3.0mm_P0.65mm")

newPart.addTag("kicadDesc", "VSSOP-8 3.0 x 3.0, http://www.ti.com/lit/ds/symlink/lm75b.pdf")
newPart.addTag("kicadTags", "VSSOP-8 3.0 x 3.0")
newPart.addTag("kicadAttr", "smd")
newPart.addTag("kicad3DModel", "${KICAD6_3DMODEL_DIR}/Package_SO.3dshapes/VSSOP-8_3.0x3.0mm_P0.65mm.wrl")

OOMP.parts.append(newPart)