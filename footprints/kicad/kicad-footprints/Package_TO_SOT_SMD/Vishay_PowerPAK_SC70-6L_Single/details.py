###### OOMP FILE  ######

import OOMP

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "kicad")
newPart.addTag("oompColor", "kicad-footprints")
newPart.addTag("oompDesc", "Package_TO_SOT_SMD")
newPart.addTag("oompIndex", "Vishay_PowerPAK_SC70-6L_Single")

newPart.addTag("kicadDesc", "Vishay PowerPAK SC70 single transistor package http://www.vishay.com/docs/70486/70486.pdf")
newPart.addTag("kicadTags", "powerpak sc70 sc-70")
newPart.addTag("kicadAttr", "smd")
newPart.addTag("kicad3DModel", "${KICAD6_3DMODEL_DIR}/Package_TO_SOT_SMD.3dshapes/Vishay_PowerPAK_SC70-6L_Single.wrl")

OOMP.parts.append(newPart)