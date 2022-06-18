###### OOMP FILE  ######

import OOMP

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "kicad")
newPart.addTag("oompColor", "kicad-footprints")
newPart.addTag("oompDesc", "Connector_Audio")
newPart.addTag("oompIndex", "Jack_XLR_Neutrik_NC4FAV-0_Vertical")

newPart.addTag("kicadDesc", "A Series, 4 pole female XLR receptacle, grounding: separate ground contact to mating connector shell and front panel, vertical PCB mount, retention spring instead of latch, https://www.neutrik.com/en/product/nc4fav-0")
newPart.addTag("kicadTags", "neutrik xlr a")
newPart.addTag("kicadAttr", "through_hole")
newPart.addTag("kicad3DModel", "${KICAD6_3DMODEL_DIR}/Connector_Audio.3dshapes/Jack_XLR_Neutrik_NC4FAV-0_Vertical.wrl")

OOMP.parts.append(newPart)