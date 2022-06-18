###### OOMP FILE  ######

import OOMP

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "kicad")
newPart.addTag("oompColor", "kicad-footprints")
newPart.addTag("oompDesc", "Connector_RJ")
newPart.addTag("oompIndex", "RJ45_BEL_SS74301-00x_Vertical")

newPart.addTag("kicadDesc", "https://belfuse.com/resources/drawings/stewartconnector/dr-stw-ss-74301-001-ss-74301-002-ss-74301-005.pdf")
newPart.addTag("kicadTags", "RJ45 Vertical Shield LED Green Yellow")
newPart.addTag("kicadAttr", "through_hole")
newPart.addTag("kicad3DModel", "${KICAD6_3DMODEL_DIR}/Connector_RJ.3dshapes/RJ45_BEL_SS74301-00x_Vertical.wrl")

OOMP.parts.append(newPart)