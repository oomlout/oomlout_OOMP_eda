###### OOMP FILE  ######

import OOMP

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "kicad")
newPart.addTag("oompColor", "kicad-footprints")
newPart.addTag("oompDesc", "Connector_Audio")
newPart.addTag("oompIndex", "Jack_XLR_Neutrik_NC3FBV1-0_Vertical")

newPart.addTag("kicadDesc", "B Series, 3 pole female XLR receptacle, grounding: mating connector shell to pin1 and front panel, vertical PCB mount, retention spring, no latch, https://www.neutrik.com/en/product/nc3fbv1-0")
newPart.addTag("kicadTags", "neutrik xlr b")
newPart.addTag("kicadAttr", "through_hole")
newPart.addTag("kicad3DModel", "${KICAD6_3DMODEL_DIR}/Connector_Audio.3dshapes/Jack_XLR_Neutrik_NC3FBV1-0_Vertical.wrl")

OOMP.parts.append(newPart)