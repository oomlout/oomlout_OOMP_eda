###### OOMP FILE  ######

import OOMP

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "kicad")
newPart.addTag("oompColor", "kicad-footprints")
newPart.addTag("oompDesc", "Package_CSP")
newPart.addTag("oompIndex", "ST_WLCSP-64_Die414")

newPart.addTag("kicadDesc", "WLCSP-64, 8x8 raster, 4.466x4.395mm package, pitch 0.5mm; see section 6.3 of http://www.st.com/resource/en/datasheet/stm32f103ze.pdf")
newPart.addTag("kicadTags", "BGA 64 0.5")
newPart.addTag("kicadAttr", "smd")
newPart.addTag("kicad3DModel", "${KICAD6_3DMODEL_DIR}/Package_CSP.3dshapes/ST_WLCSP-64_Die414.wrl")

OOMP.parts.append(newPart)