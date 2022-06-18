###### OOMP FILE  ######

import OOMP

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "kicad")
newPart.addTag("oompColor", "kicad-footprints")
newPart.addTag("oompDesc", "Package_TO_SOT_SMD")
newPart.addTag("oompIndex", "TO-252-2")

newPart.addTag("kicadDesc", "TO-252 / DPAK SMD package, http://www.infineon.com/cms/en/product/packages/PG-TO252/PG-TO252-3-1/")
newPart.addTag("kicadTags", "DPAK TO-252 DPAK-3 TO-252-3 SOT-428")
newPart.addTag("kicadAttr", "smd")
newPart.addTag("kicad3DModel", "${KICAD6_3DMODEL_DIR}/Package_TO_SOT_SMD.3dshapes/TO-252-2.wrl")

OOMP.parts.append(newPart)