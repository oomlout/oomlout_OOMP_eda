###### OOMP FILE  ######

import OOMP

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "kicad")
newPart.addTag("oompColor", "kicad-footprints")
newPart.addTag("oompDesc", "Package_BGA")
newPart.addTag("oompIndex", "LFBGA-100_10x10mm_Layout10x10_P0.8mm")

newPart.addTag("kicadDesc", "LFBGA-100, 10x10 raster, 10x10mm package, pitch 0.8mm; see section 6.3 of http://www.st.com/resource/en/datasheet/stm32f103tb.pdf")
newPart.addTag("kicadTags", "BGA 100 0.8")
newPart.addTag("kicadAttr", "smd")
newPart.addTag("kicad3DModel", "${KICAD6_3DMODEL_DIR}/Package_BGA.3dshapes/LFBGA-100_10x10mm_Layout10x10_P0.8mm.wrl")

OOMP.parts.append(newPart)