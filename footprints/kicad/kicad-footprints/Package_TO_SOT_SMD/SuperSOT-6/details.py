###### OOMP FILE  ######

import OOMP

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "kicad")
newPart.addTag("oompColor", "kicad-footprints")
newPart.addTag("oompDesc", "Package_TO_SOT_SMD")
newPart.addTag("oompIndex", "SuperSOT-6")

newPart.addTag("kicadDesc", "6-pin SuperSOT package http://www.mouser.com/ds/2/149/FMB5551-889214.pdf")
newPart.addTag("kicadTags", "SuperSOT-6 SSOT-6")
newPart.addTag("kicadAttr", "smd")
newPart.addTag("kicad3DModel", "${KICAD6_3DMODEL_DIR}/Package_TO_SOT_SMD.3dshapes/SuperSOT-6.wrl")

OOMP.parts.append(newPart)