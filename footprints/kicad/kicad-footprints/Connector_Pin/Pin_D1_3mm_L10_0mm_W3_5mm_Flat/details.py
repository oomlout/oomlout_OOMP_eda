###### OOMP FILE  ######

import OOMP

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "kicad")
newPart.addTag("oompColor", "kicad-footprints")
newPart.addTag("oompDesc", "Connector_Pin")
newPart.addTag("oompIndex", "Pin_D1.3mm_L10.0mm_W3.5mm_Flat")

newPart.addTag("kicadDesc", "solder Pin_ with flat with hole, hole diameter 1.3mm, length 10.0mm, width 3.5mm, e.g. Ettinger 13.13.865, https://katalog.ettinger.de/#p=434")
newPart.addTag("kicadTags", "solder Pin_ with flat fork")
newPart.addTag("kicadAttr", "through_hole")
newPart.addTag("kicad3DModel", "${KICAD6_3DMODEL_DIR}/Connector_Pin.3dshapes/Pin_D1.3mm_L10.0mm_W3.5mm_Flat.wrl")

OOMP.parts.append(newPart)