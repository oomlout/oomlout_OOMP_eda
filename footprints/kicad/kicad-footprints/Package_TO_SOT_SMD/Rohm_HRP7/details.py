###### OOMP FILE  ######

import OOMP

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "kicad")
newPart.addTag("oompColor", "kicad-footprints")
newPart.addTag("oompDesc", "Package_TO_SOT_SMD")
newPart.addTag("oompIndex", "Rohm_HRP7")

newPart.addTag("kicadDesc", "Rohm HRP7 SMD package, http://rohmfs.rohm.com/en/techdata_basic/ic/package/hrp7_1-e.pdf, http://rohmfs.rohm.com/en/products/databook/datasheet/ic/motor/dc/bd621x-e.pdf")
newPart.addTag("kicadTags", "Rohm HRP7 SMD")
newPart.addTag("kicadAttr", "smd")
newPart.addTag("kicad3DModel", "${KICAD6_3DMODEL_DIR}/Package_TO_SOT_SMD.3dshapes/Rohm_HRP7.wrl")

OOMP.parts.append(newPart)