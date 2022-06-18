###### OOMP FILE  ######

import OOMP

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "kicad")
newPart.addTag("oompColor", "kicad-footprints")
newPart.addTag("oompDesc", "Package_CSP")
newPart.addTag("oompIndex", "ST_WLCSP-25_Die457")

newPart.addTag("kicadDesc", "WLCSP-25, 5x5 raster, 2.133x2.070mm package, pitch 0.4mm; see section 7.3 of http://www.st.com/resource/en/datasheet/stm32l011k3.pdf")
newPart.addTag("kicadTags", "BGA 25 0.4")
newPart.addTag("kicadAttr", "smd")
newPart.addTag("kicad3DModel", "${KICAD6_3DMODEL_DIR}/Package_CSP.3dshapes/ST_WLCSP-25_Die457.wrl")

OOMP.parts.append(newPart)