###### OOMP FILE  ######

import OOMP

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "kicad")
newPart.addTag("oompColor", "kicad-footprints")
newPart.addTag("oompDesc", "Connector_Pin")
newPart.addTag("oompIndex", "Pin_D1.3mm_L11.0mm")

newPart.addTag("kicadDesc", "solder Pin_ diameter 1.3mm, hole diameter 1.3mm, length 11.0mm")
newPart.addTag("kicadTags", "solder Pin_ pressfit")
newPart.addTag("kicadAttr", "through_hole")
newPart.addTag("kicad3DModel", "${KICAD6_3DMODEL_DIR}/Connector_Pin.3dshapes/Pin_D1.3mm_L11.0mm.wrl")

OOMP.parts.append(newPart)