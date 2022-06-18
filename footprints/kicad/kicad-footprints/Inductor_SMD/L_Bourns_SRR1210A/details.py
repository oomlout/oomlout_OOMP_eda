###### OOMP FILE  ######

import OOMP

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "kicad")
newPart.addTag("oompColor", "kicad-footprints")
newPart.addTag("oompDesc", "Inductor_SMD")
newPart.addTag("oompIndex", "L_Bourns_SRR1210A")

newPart.addTag("kicadDesc", "Bourns SRR1210A series SMD inductor https://www.bourns.com/docs/Product-Datasheets/SRR1210A.pdf")
newPart.addTag("kicadTags", "Bourns SRR1210A SMD inductor")
newPart.addTag("kicadAttr", "smd")
newPart.addTag("kicad3DModel", "${KICAD6_3DMODEL_DIR}/Inductor_SMD.3dshapes/L_Bourns_SRR1210A.wrl")

OOMP.parts.append(newPart)