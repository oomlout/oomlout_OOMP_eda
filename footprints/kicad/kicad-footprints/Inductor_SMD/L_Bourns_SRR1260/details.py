###### OOMP FILE  ######

import OOMP

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "kicad")
newPart.addTag("oompColor", "kicad-footprints")
newPart.addTag("oompDesc", "Inductor_SMD")
newPart.addTag("oompIndex", "L_Bourns_SRR1260")

newPart.addTag("kicadDesc", "Bourns SRR1260 series SMD inductor http://www.bourns.com/docs/Product-Datasheets/SRR1260.pdf")
newPart.addTag("kicadTags", "Bourns SRR1260 SMD inductor")
newPart.addTag("kicadAttr", "smd")
newPart.addTag("kicad3DModel", "${KICAD6_3DMODEL_DIR}/Inductor_SMD.3dshapes/L_Bourns_SRR1260.wrl")

OOMP.parts.append(newPart)