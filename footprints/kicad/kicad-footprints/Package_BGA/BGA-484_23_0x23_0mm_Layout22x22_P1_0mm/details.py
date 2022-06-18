###### OOMP FILE  ######

import OOMP

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "kicad")
newPart.addTag("oompColor", "kicad-footprints")
newPart.addTag("oompDesc", "Package_BGA")
newPart.addTag("oompIndex", "BGA-484_23.0x23.0mm_Layout22x22_P1.0mm")

newPart.addTag("kicadDesc", "BGA-484, https://www.xilinx.com/support/documentation/package_specs/fg484.pdf")
newPart.addTag("kicadTags", "BGA-484")
newPart.addTag("kicadAttr", "smd")
newPart.addTag("kicad3DModel", "${KICAD6_3DMODEL_DIR}/Package_BGA.3dshapes/BGA-484_23.0x23.0mm_Layout22x22_P1.0mm.wrl")

OOMP.parts.append(newPart)