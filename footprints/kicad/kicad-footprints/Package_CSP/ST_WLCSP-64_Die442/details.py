###### OOMP FILE  ######

import OOMP

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "kicad")
newPart.addTag("oompColor", "kicad-footprints")
newPart.addTag("oompDesc", "Package_CSP")
newPart.addTag("oompIndex", "ST_WLCSP-64_Die442")

newPart.addTag("kicadDesc", "WLCSP-64, 8x8 raster, 3.347x3.585mm package, pitch 0.4mm; see section 7.4 of http://www.st.com/resource/en/datasheet/stm32f091vb.pdf")
newPart.addTag("kicadTags", "BGA 64 0.4")
newPart.addTag("kicadAttr", "smd")
newPart.addTag("kicad3DModel", "${KICAD6_3DMODEL_DIR}/Package_CSP.3dshapes/ST_WLCSP-64_Die442.wrl")

OOMP.parts.append(newPart)