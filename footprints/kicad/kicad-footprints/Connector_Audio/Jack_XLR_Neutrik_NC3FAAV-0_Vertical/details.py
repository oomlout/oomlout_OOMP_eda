###### OOMP FILE  ######

import OOMP

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "kicad")
newPart.addTag("oompColor", "kicad-footprints")
newPart.addTag("oompDesc", "Connector_Audio")
newPart.addTag("oompIndex", "Jack_XLR_Neutrik_NC3FAAV-0_Vertical")

newPart.addTag("kicadDesc", "AA Series, 3 pole female receptacle, grounding: without ground/shell contact, vertical PCB mount, retention spring instead of latch, https://www.neutrik.com/en/product/nc3faav-0")
newPart.addTag("kicadTags", "neutrik xlr aa")
newPart.addTag("kicadAttr", "through_hole")
newPart.addTag("kicad3DModel", "${KICAD6_3DMODEL_DIR}/Connector_Audio.3dshapes/Jack_XLR_Neutrik_NC3FAAV-0_Vertical.wrl")

OOMP.parts.append(newPart)