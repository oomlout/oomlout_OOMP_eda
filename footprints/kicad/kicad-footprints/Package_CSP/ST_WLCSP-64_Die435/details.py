###### OOMP FILE  ######

import OOMP

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "kicad")
newPart.addTag("oompColor", "kicad-footprints")
newPart.addTag("oompDesc", "Package_CSP")
newPart.addTag("oompIndex", "ST_WLCSP-64_Die435")

newPart.addTag("kicadDesc", "WLCSP-64, 8x8 raster, 3.141x3.127mm package, pitch 0.35mm; see section 7.5 of http://www.st.com/resource/en/datasheet/DM00257211.pdf")
newPart.addTag("kicadTags", "BGA 64 0.35")
newPart.addTag("kicadAttr", "smd")
newPart.addTag("kicad3DModel", "${KICAD6_3DMODEL_DIR}/Package_CSP.3dshapes/ST_WLCSP-64_Die435.wrl")

OOMP.parts.append(newPart)