###### OOMP FILE  ######

import OOMP

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "kicad")
newPart.addTag("oompColor", "kicad-footprints")
newPart.addTag("oompDesc", "Package_CSP")
newPart.addTag("oompIndex", "ST_WLCSP-144_Die470")

newPart.addTag("kicadDesc", "WLCSP-144, 12x12 raster, 5.24x5.24mm package, pitch 0.4mm; see section 7.4 of http://www.st.com/resource/en/datasheet/DM00366448.pdf")
newPart.addTag("kicadTags", "BGA 144 0.4")
newPart.addTag("kicadAttr", "smd")
newPart.addTag("kicad3DModel", "${KICAD6_3DMODEL_DIR}/Package_CSP.3dshapes/ST_WLCSP-144_Die470.wrl")

OOMP.parts.append(newPart)