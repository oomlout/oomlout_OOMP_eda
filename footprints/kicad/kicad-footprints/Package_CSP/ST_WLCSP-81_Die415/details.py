###### OOMP FILE  ######

import OOMP

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "kicad")
newPart.addTag("oompColor", "kicad-footprints")
newPart.addTag("oompDesc", "Package_CSP")
newPart.addTag("oompIndex", "ST_WLCSP-81_Die415")

newPart.addTag("kicadDesc", "WLCSP-81, 9x9 raster, 4.4084x3.7594mm package, pitch 0.4mm; see section 7.4 of http://www.st.com/resource/en/datasheet/stm32l476me.pdf")
newPart.addTag("kicadTags", "BGA 81 0.4")
newPart.addTag("kicadAttr", "smd")
newPart.addTag("kicad3DModel", "${KICAD6_3DMODEL_DIR}/Package_CSP.3dshapes/ST_WLCSP-81_Die415.wrl")

OOMP.parts.append(newPart)