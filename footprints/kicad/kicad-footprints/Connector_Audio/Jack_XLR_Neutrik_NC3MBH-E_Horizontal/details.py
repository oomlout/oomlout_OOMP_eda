###### OOMP FILE  ######

import OOMP

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "kicad")
newPart.addTag("oompColor", "kicad-footprints")
newPart.addTag("oompDesc", "Connector_Audio")
newPart.addTag("oompIndex", "Jack_XLR_Neutrik_NC3MBH-E_Horizontal")

newPart.addTag("kicadDesc", "B Series, 3 pole male XLR receptacle, grounding: separate ground contact to mating connector shell and front panel, steel retention lug, horizontal PCB mount, additional ground contacts, https://www.neutrik.com/en/product/nc3mbh-e")
newPart.addTag("kicadTags", "neutrik xlr b")
newPart.addTag("kicadAttr", "through_hole")
newPart.addTag("kicad3DModel", "${KICAD6_3DMODEL_DIR}/Connector_Audio.3dshapes/Jack_XLR_Neutrik_NC3MBH-E_Horizontal.wrl")

OOMP.parts.append(newPart)