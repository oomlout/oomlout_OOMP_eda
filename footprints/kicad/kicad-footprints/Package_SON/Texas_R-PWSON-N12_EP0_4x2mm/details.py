###### OOMP FILE  ######

import OOMP

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "kicad")
newPart.addTag("oompColor", "kicad-footprints")
newPart.addTag("oompDesc", "Package_SON")
newPart.addTag("oompIndex", "Texas_R-PWSON-N12_EP0.4x2mm")

newPart.addTag("kicadDesc", "http://www.ti.com/lit/ds/symlink/tpd6f003.pdf")
newPart.addTag("kicadTags", "WSON SMD")
newPart.addTag("kicadAttr", "smd")
newPart.addTag("kicad3DModel", "${KICAD6_3DMODEL_DIR}/Package_SON.3dshapes/Texas_R-PWSON-N12_EP0.4x2mm.wrl")

OOMP.parts.append(newPart)