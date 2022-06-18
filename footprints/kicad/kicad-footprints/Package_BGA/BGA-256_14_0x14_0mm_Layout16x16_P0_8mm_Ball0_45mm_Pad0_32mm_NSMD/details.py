###### OOMP FILE  ######

import OOMP

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "kicad")
newPart.addTag("oompColor", "kicad-footprints")
newPart.addTag("oompDesc", "Package_BGA")
newPart.addTag("oompIndex", "BGA-256_14.0x14.0mm_Layout16x16_P0.8mm_Ball0.45mm_Pad0.32mm_NSMD")

newPart.addTag("kicadDesc", "BGA-256, dimensions: https://www.xilinx.com/support/documentation/package_specs/ft256.pdf, design rules: https://www.xilinx.com/support/documentation/user_guides/ug1099-bga-device-design-rules.pdf")
newPart.addTag("kicadTags", "BGA-256")
newPart.addTag("kicadAttr", "smd")
newPart.addTag("kicad3DModel", "${KICAD6_3DMODEL_DIR}/Package_BGA.3dshapes/BGA-256_14.0x14.0mm_Layout16x16_P0.8mm_Ball0.45mm_Pad0.32mm_NSMD.wrl")

OOMP.parts.append(newPart)