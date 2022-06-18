###### OOMP FILE  ######

import OOMP

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "kicad")
newPart.addTag("oompColor", "kicad-footprints")
newPart.addTag("oompDesc", "Inductor_SMD")
newPart.addTag("oompIndex", "L_Bourns_SRN6045TA")

newPart.addTag("kicadDesc", "http://www.bourns.com/docs/product-datasheets/srn6045ta.pdf")
newPart.addTag("kicadTags", "Semi-shielded Power Inductor")
newPart.addTag("kicadAttr", "smd")
newPart.addTag("kicad3DModel", "${KICAD6_3DMODEL_DIR}/Inductor_SMD.3dshapes/L_Bourns_SRN6045TA.wrl")

OOMP.parts.append(newPart)