###### OOMP FILE  ######

import OOMP

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "kicad")
newPart.addTag("oompColor", "kicad-footprints")
newPart.addTag("oompDesc", "Connector_Audio")
newPart.addTag("oompIndex", "Jack_XLR_Neutrik_NC3FAAH1-DA_Horizontal")

newPart.addTag("kicadDesc", "AA Series, 3 pole female XLR receptacle, grounding: mating connector shell to pin1 and front panel, horizontal PCB mount, asymmetric push, https://www.neutrik.com/en/product/nc3faah1-da")
newPart.addTag("kicadTags", "neutrik xlr aa")
newPart.addTag("kicadAttr", "through_hole")
newPart.addTag("kicad3DModel", "${KICAD6_3DMODEL_DIR}/Connector_Audio.3dshapes/Jack_XLR_Neutrik_NC3FAAH1-DA_Horizontal.wrl")

OOMP.parts.append(newPart)