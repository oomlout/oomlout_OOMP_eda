###### OOMP FILE  ######

import OOMP

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "kicad")
newPart.addTag("oompColor", "kicad-footprints")
newPart.addTag("oompDesc", "Package_TO_SOT_SMD")
newPart.addTag("oompIndex", "OnSemi_ECH8")

newPart.addTag("kicadDesc", "On Semiconductor ECH8, https://www.onsemi.com/pub/Collateral/318BF.PDF")
newPart.addTag("kicadTags", "ECH8 SOT28-FL SOT-28-FL")
newPart.addTag("kicadAttr", "smd")
newPart.addTag("kicad3DModel", "${KICAD6_3DMODEL_DIR}/Package_TO_SOT_SMD.3dshapes/OnSemi_ECH8.wrl")

OOMP.parts.append(newPart)