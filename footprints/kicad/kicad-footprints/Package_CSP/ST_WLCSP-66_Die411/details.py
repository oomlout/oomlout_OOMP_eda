###### OOMP FILE  ######

import OOMP

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "kicad")
newPart.addTag("oompColor", "kicad-footprints")
newPart.addTag("oompDesc", "Package_CSP")
newPart.addTag("oompIndex", "ST_WLCSP-66_Die411")

newPart.addTag("kicadDesc", "WLCSP-66, 9x9 raster, 3.639x3.971mm package, pitch 0.4mm; see section 7.2 of http://www.st.com/resource/en/datasheet/stm32f207vg.pdf")
newPart.addTag("kicadTags", "BGA 66 0.4")
newPart.addTag("kicadAttr", "smd")
newPart.addTag("kicad3DModel", "${KICAD6_3DMODEL_DIR}/Package_CSP.3dshapes/ST_WLCSP-66_Die411.wrl")

OOMP.parts.append(newPart)