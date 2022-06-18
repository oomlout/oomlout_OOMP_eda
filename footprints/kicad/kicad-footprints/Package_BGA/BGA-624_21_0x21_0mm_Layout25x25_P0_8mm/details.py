###### OOMP FILE  ######

import OOMP

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "kicad")
newPart.addTag("oompColor", "kicad-footprints")
newPart.addTag("oompDesc", "Package_BGA")
newPart.addTag("oompIndex", "BGA-624_21.0x21.0mm_Layout25x25_P0.8mm")
newPart.addTag("oompName", "kicad-footprints/Package_BGA/BGA-624_21.0x21.0mm_Layout25x25_P0.8mm")

newPart.addTag("kicadDesc", "BGA-624, 25x25 grid, 21x21mm package, pitch 0.8mm; https://www.nxp.com/docs/en/package-information/SOT1529-1.pdf")
newPart.addTag("kicadTags", "BGA 624 0.8")
newPart.addTag("kicadAttr", "smd")
newPart.addTag("kicad3DModel", "${KICAD6_3DMODEL_DIR}/Package_BGA.3dshapes/BGA-624_21.0x21.0mm_Layout25x25_P0.8mm.wrl")

OOMP.parts.append(newPart)