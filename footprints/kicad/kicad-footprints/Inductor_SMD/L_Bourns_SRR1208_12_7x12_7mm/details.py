###### OOMP FILE  ######

import OOMP

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "kicad")
newPart.addTag("oompColor", "kicad-footprints")
newPart.addTag("oompDesc", "Inductor_SMD")
newPart.addTag("oompIndex", "L_Bourns_SRR1208_12.7x12.7mm")

newPart.addTag("kicadDesc", "Bourns SRP1208 series SMD inductor https://www.bourns.com/pdfs/SRR1208.pdf")
newPart.addTag("kicadTags", "Bourns SRP1208 SMD inductor")
newPart.addTag("kicadAttr", "smd")
newPart.addTag("kicad3DModel", "${KICAD6_3DMODEL_DIR}/Inductor_SMD.3dshapes/L_Bourns_SRR1208_12.7x12.7mm.wrl")

OOMP.parts.append(newPart)