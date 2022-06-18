###### OOMP FILE  ######

import OOMP

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "kicad")
newPart.addTag("oompColor", "kicad-footprints")
newPart.addTag("oompDesc", "Package_BGA")
newPart.addTag("oompIndex", "XFBGA-121_8x8mm_Layout11x11_P0.65mm")

newPart.addTag("kicadDesc", "XFBGA-121, https://www.nxp.com/docs/en/package-information/SOT1533-1.pdf")
newPart.addTag("kicadTags", "XFBGA-121")
newPart.addTag("kicadAttr", "smd")
newPart.addTag("kicad3DModel", "${KICAD6_3DMODEL_DIR}/Package_BGA.3dshapes/XFBGA-121_8x8mm_Layout11x11_P0.65mm.wrl")

OOMP.parts.append(newPart)