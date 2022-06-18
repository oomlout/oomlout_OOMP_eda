###### OOMP FILE  ######

import OOMP

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "kicad")
newPart.addTag("oompColor", "kicad-footprints")
newPart.addTag("oompDesc", "Inductor_SMD")
newPart.addTag("oompIndex", "L_Bourns_SRP1245A")

newPart.addTag("kicadDesc", "Bourns SRP1245A series SMD inductor http://www.bourns.com/docs/Product-Datasheets/SRP1245A.pdf")
newPart.addTag("kicadTags", "Bourns SRP1245A SMD inductor")
newPart.addTag("kicadAttr", "smd")
newPart.addTag("kicad3DModel", "${KICAD6_3DMODEL_DIR}/Inductor_SMD.3dshapes/L_Bourns_SRP1245A.wrl")

OOMP.parts.append(newPart)