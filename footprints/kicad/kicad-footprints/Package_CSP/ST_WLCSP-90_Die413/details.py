###### OOMP FILE  ######

import OOMP

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "kicad")
newPart.addTag("oompColor", "kicad-footprints")
newPart.addTag("oompDesc", "Package_CSP")
newPart.addTag("oompIndex", "ST_WLCSP-90_Die413")

newPart.addTag("kicadDesc", "WLCSP-90, 10x9 raster, 4.223x3.969mm package, pitch 0.4mm; see section 6.1 of http://www.st.com/resource/en/datasheet/stm32f405og.pdf")
newPart.addTag("kicadTags", "BGA 90 0.4")
newPart.addTag("kicadAttr", "smd")
newPart.addTag("kicad3DModel", "${KICAD6_3DMODEL_DIR}/Package_CSP.3dshapes/ST_WLCSP-90_Die413.wrl")

OOMP.parts.append(newPart)