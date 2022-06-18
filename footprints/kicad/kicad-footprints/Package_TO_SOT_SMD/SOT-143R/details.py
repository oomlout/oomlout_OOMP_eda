###### OOMP FILE  ######

import OOMP

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "kicad")
newPart.addTag("oompColor", "kicad-footprints")
newPart.addTag("oompDesc", "Package_TO_SOT_SMD")
newPart.addTag("oompIndex", "SOT-143R")

newPart.addTag("kicadDesc", "SOT-143R, reverse pinning, https://www.nxp.com/docs/en/package-information/SOT143R.pdf")
newPart.addTag("kicadTags", "SOT-143R Reverse")
newPart.addTag("kicadAttr", "smd")
newPart.addTag("kicad3DModel", "${KICAD6_3DMODEL_DIR}/Package_TO_SOT_SMD.3dshapes/SOT-143R.wrl")

OOMP.parts.append(newPart)