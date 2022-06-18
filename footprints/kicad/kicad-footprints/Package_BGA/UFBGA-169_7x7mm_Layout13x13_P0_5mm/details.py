###### OOMP FILE  ######

import OOMP

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "kicad")
newPart.addTag("oompColor", "kicad-footprints")
newPart.addTag("oompDesc", "Package_BGA")
newPart.addTag("oompIndex", "UFBGA-169_7x7mm_Layout13x13_P0.5mm")

newPart.addTag("kicadDesc", "UFBGA-169, 13x13 raster, 7x7mm package, pitch 0.5mm; see section 7.6 of http://www.st.com/resource/en/datasheet/stm32f429ng.pdf")
newPart.addTag("kicadTags", "BGA 169 0.5")
newPart.addTag("kicadAttr", "smd")
newPart.addTag("kicad3DModel", "${KICAD6_3DMODEL_DIR}/Package_BGA.3dshapes/UFBGA-169_7x7mm_Layout13x13_P0.5mm.wrl")

OOMP.parts.append(newPart)