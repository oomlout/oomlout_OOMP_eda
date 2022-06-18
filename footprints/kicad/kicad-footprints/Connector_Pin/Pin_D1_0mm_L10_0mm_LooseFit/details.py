###### OOMP FILE  ######

import OOMP

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "kicad")
newPart.addTag("oompColor", "kicad-footprints")
newPart.addTag("oompDesc", "Connector_Pin")
newPart.addTag("oompIndex", "Pin_D1.0mm_L10.0mm_LooseFit")

newPart.addTag("kicadDesc", "solder Pin_ diameter 1.0mm, hole diameter 1.2mm (loose fit), length 10.0mm")
newPart.addTag("kicadTags", "solder Pin_ loose fit")
newPart.addTag("kicadAttr", "through_hole")
newPart.addTag("kicad3DModel", "${KICAD6_3DMODEL_DIR}/Connector_Pin.3dshapes/Pin_D1.0mm_L10.0mm_LooseFit.wrl")

OOMP.parts.append(newPart)