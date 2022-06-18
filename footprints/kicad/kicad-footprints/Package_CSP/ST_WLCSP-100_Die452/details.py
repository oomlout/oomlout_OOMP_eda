###### OOMP FILE  ######

import OOMP

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "kicad")
newPart.addTag("oompColor", "kicad-footprints")
newPart.addTag("oompDesc", "Package_CSP")
newPart.addTag("oompIndex", "ST_WLCSP-100_Die452")

newPart.addTag("kicadDesc", "WLCSP-100, 10x10 raster, 4.201x4.663mm package, pitch 0.4mm; see section 7.7 of http://www.st.com/resource/en/datasheet/DM00330506.pdf")
newPart.addTag("kicadTags", "BGA 100 0.4")
newPart.addTag("kicadAttr", "smd")
newPart.addTag("kicad3DModel", "${KICAD6_3DMODEL_DIR}/Package_CSP.3dshapes/ST_WLCSP-100_Die452.wrl")

OOMP.parts.append(newPart)