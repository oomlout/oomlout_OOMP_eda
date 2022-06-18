###### OOMP FILE  ######

import OOMP

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "kicad")
newPart.addTag("oompColor", "kicad-footprints")
newPart.addTag("oompDesc", "Connector_USB")
newPart.addTag("oompIndex", "USB_A_Stewart_SS-52100-001_Horizontal")

newPart.addTag("kicadDesc", "USB A connector https://belfuse.com/resources/drawings/stewartconnector/dr-stw-ss-52100-001.pdf")
newPart.addTag("kicadTags", "USB_A Female Connector receptacle")
newPart.addTag("kicadAttr", "through_hole")
newPart.addTag("kicad3DModel", "${KICAD6_3DMODEL_DIR}/Connector_USB.3dshapes/USB_A_Stewart_SS-52100-001_Horizontal.wrl")

OOMP.parts.append(newPart)