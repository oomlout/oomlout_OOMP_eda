###### OOMP FILE  ######

import OOMP

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "kicad")
newPart.addTag("oompColor", "kicad-footprints")
newPart.addTag("oompDesc", "Package_BGA")
newPart.addTag("oompIndex", "TFBGA-265_14x14mm_Layout17x17_P0.8mm")

newPart.addTag("kicadDesc", "TFBGA-265, 17x17 raster, 14x14mm package, pitch 0.8mm; see section 7.8 of http://www.st.com/resource/en/datasheet/DM00387108.pdf")
newPart.addTag("kicadTags", "BGA 265 0.8")
newPart.addTag("kicadAttr", "smd")
newPart.addTag("kicad3DModel", "${KICAD6_3DMODEL_DIR}/Package_BGA.3dshapes/TFBGA-265_14x14mm_Layout17x17_P0.8mm.wrl")

OOMP.parts.append(newPart)