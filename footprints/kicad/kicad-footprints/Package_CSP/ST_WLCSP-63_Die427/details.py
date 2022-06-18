###### OOMP FILE  ######

import OOMP

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "kicad")
newPart.addTag("oompColor", "kicad-footprints")
newPart.addTag("oompDesc", "Package_CSP")
newPart.addTag("oompIndex", "ST_WLCSP-63_Die427")

newPart.addTag("kicadDesc", "WLCSP-63, 7x9 raster, 3.228x4.164mm package, pitch 0.4mm; see section 7.6 of http://www.st.com/resource/en/datasheet/stm32l151cc.pdf")
newPart.addTag("kicadTags", "BGA 63 0.4")
newPart.addTag("kicadAttr", "smd")
newPart.addTag("kicad3DModel", "${KICAD6_3DMODEL_DIR}/Package_CSP.3dshapes/ST_WLCSP-63_Die427.wrl")

OOMP.parts.append(newPart)