###### OOMP FILE  ######

import OOMP

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "kicad")
newPart.addTag("oompColor", "kicad-footprints")
newPart.addTag("oompDesc", "Inductor_THT")
newPart.addTag("oompIndex", "Choke_EPCOS_B82722A")

newPart.addTag("kicadDesc", "Current-Compensated Ring Core Double Chokes, EPCOS, B82722A, 22.3mmx22.7mm, https://en.tdk.eu/inf/30/db/ind_2008/b82722a_j.pdf")
newPart.addTag("kicadTags", "chokes epcos tht")
newPart.addTag("kicadAttr", "through_hole")
newPart.addTag("kicad3DModel", "${KICAD6_3DMODEL_DIR}/Inductor_THT.3dshapes/Choke_EPCOS_B82722A.wrl")

OOMP.parts.append(newPart)