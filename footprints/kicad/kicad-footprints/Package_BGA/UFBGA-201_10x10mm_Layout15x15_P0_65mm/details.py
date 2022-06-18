###### OOMP FILE  ######

import OOMP

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "kicad")
newPart.addTag("oompColor", "kicad-footprints")
newPart.addTag("oompDesc", "Package_BGA")
newPart.addTag("oompIndex", "UFBGA-201_10x10mm_Layout15x15_P0.65mm")
newPart.addTag("oompName", "kicad-footprints/Package_BGA/UFBGA-201_10x10mm_Layout15x15_P0.65mm")

newPart.addTag("kicadDesc", "UFBGA-201, 15x15 raster, 10x10mm package, pitch 0.65mm; see section 7.6 of http://www.st.com/resource/en/datasheet/stm32f207vg.pdf")
newPart.addTag("kicadTags", "BGA 201 0.65")
newPart.addTag("kicadAttr", "smd")
newPart.addTag("kicad3DModel", "${KICAD6_3DMODEL_DIR}/Package_BGA.3dshapes/UFBGA-201_10x10mm_Layout15x15_P0.65mm.wrl")

OOMP.parts.append(newPart)