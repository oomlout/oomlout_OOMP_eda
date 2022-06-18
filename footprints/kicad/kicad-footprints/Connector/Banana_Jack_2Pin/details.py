###### OOMP FILE  ######

import OOMP

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "kicad")
newPart.addTag("oompColor", "kicad-footprints")
newPart.addTag("oompDesc", "Connector")
newPart.addTag("oompIndex", "Banana_Jack_2Pin")

newPart.addTag("kicadDesc", "Dual banana socket, footprint - 2 x 6mm drills")
newPart.addTag("kicadTags", "banana socket")
newPart.addTag("kicadAttr", "through_hole")
newPart.addTag("kicad3DModel", "${KICAD6_3DMODEL_DIR}/Connector.3dshapes/Banana_Jack_2Pin.wrl")

OOMP.parts.append(newPart)