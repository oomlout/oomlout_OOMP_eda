###### OOMP FILE  ######

import OOMP

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "kicad")
newPart.addTag("oompColor", "kicad-footprints")
newPart.addTag("oompDesc", "Inductor_SMD")
newPart.addTag("oompIndex", "L_Bourns-SRN8040_8x8.15mm")

newPart.addTag("kicadDesc", "Bourns SRN8040 series SMD inductor 8x8.15mm, https://www.bourns.com/docs/Product-Datasheets/SRN8040.pdf")
newPart.addTag("kicadTags", "Bourns SRN8040 SMD inductor")
newPart.addTag("kicadAttr", "smd")
newPart.addTag("kicad3DModel", "${KICAD6_3DMODEL_DIR}/Inductor_SMD.3dshapes/L_Bourns-SRN8040_8x8.15mm.wrl")

OOMP.parts.append(newPart)