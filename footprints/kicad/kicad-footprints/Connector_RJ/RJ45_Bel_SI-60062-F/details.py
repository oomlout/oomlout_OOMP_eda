###### OOMP FILE  ######

import OOMP

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "kicad")
newPart.addTag("oompColor", "kicad-footprints")
newPart.addTag("oompDesc", "Connector_RJ")
newPart.addTag("oompIndex", "RJ45_Bel_SI-60062-F")

newPart.addTag("kicadDesc", "1 Port RJ45 Magjack Connector Through Hole 10/100 Base-T, AutoMDIX, https://belfuse.com/resources/drawings/magneticsolutions/dr-mag-si-60062-f.pdf")
newPart.addTag("kicadTags", "RJ45 Magjack")
newPart.addTag("kicadAttr", "through_hole")
newPart.addTag("kicad3DModel", "${KICAD6_3DMODEL_DIR}/Connector_RJ.3dshapes/RJ45_Bel_SI-60062-F.wrl")

OOMP.parts.append(newPart)