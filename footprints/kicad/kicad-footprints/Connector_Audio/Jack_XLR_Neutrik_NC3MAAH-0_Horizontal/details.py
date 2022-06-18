###### OOMP FILE  ######

import OOMP

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "kicad")
newPart.addTag("oompColor", "kicad-footprints")
newPart.addTag("oompDesc", "Connector_Audio")
newPart.addTag("oompIndex", "Jack_XLR_Neutrik_NC3MAAH-0_Horizontal")

newPart.addTag("kicadDesc", "AA Series, 3 pole male XLR receptacle, grounding: ground contact connected to shell ground, but not to front panel and Pin 1, horizontal PCB mount, https://www.neutrik.com/en/product/nc3maah-0")
newPart.addTag("kicadTags", "neutrik xlr aa")
newPart.addTag("kicadAttr", "through_hole")
newPart.addTag("kicad3DModel", "${KICAD6_3DMODEL_DIR}/Connector_Audio.3dshapes/Jack_XLR_Neutrik_NC3MAAH-0_Horizontal.wrl")

OOMP.parts.append(newPart)