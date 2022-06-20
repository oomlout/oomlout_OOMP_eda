###### OOMP FILE  ######

import OOMP

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "kicad")
newPart.addTag("oompColor", "kicad-footprints")
newPart.addTag("oompDesc", "Package_BGA")
newPart.addTag("oompIndex", "UFBGA-132_7x7mm_Layout12x12_P0.5mm")
newPart.addTag("oompName", "kicad-footprints/Package_BGA/UFBGA-132_7x7mm_Layout12x12_P0.5mm")

newPart.addTag("kicadDesc", "UFBGA-132, 12x12 raster, 7x7mm package, pitch 0.5mm; see section 7.4 of http://www.st.com/resource/en/datasheet/stm32l152zc.pdf")
newPart.addTag("kicadTags", "BGA 132 0.5")
newPart.addTag("kicadAttr", "smd")
newPart.addTag("kicad3DModel", "${KICAD6_3DMODEL_DIR}/Package_BGA.3dshapes/UFBGA-132_7x7mm_Layout12x12_P0.5mm.wrl")

OOMP.parts.append(newPart)