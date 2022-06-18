###### OOMP FILE  ######

import OOMP

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "kicad")
newPart.addTag("oompColor", "kicad-footprints")
newPart.addTag("oompDesc", "Package_BGA")
newPart.addTag("oompIndex", "TFBGA-64_5x5mm_Layout8x8_P0.5mm")
newPart.addTag("oompName", "kicad-footprints/Package_BGA/TFBGA-64_5x5mm_Layout8x8_P0.5mm")

newPart.addTag("kicadDesc", "TFBGA-64, 8x8 raster, 5x5mm package, pitch 0.5mm; see section 6.3 of http://www.st.com/resource/en/datasheet/stm32f100v8.pdf")
newPart.addTag("kicadTags", "BGA 64 0.5")
newPart.addTag("kicadAttr", "smd")
newPart.addTag("kicad3DModel", "${KICAD6_3DMODEL_DIR}/Package_BGA.3dshapes/TFBGA-64_5x5mm_Layout8x8_P0.5mm.wrl")

OOMP.parts.append(newPart)