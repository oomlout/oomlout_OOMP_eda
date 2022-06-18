###### OOMP FILE  ######

import OOMP

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "kicad")
newPart.addTag("oompColor", "kicad-footprints")
newPart.addTag("oompDesc", "Package_LCC")
newPart.addTag("oompIndex", "PLCC-44_THT-Socket")

newPart.addTag("kicadDesc", "PLCC, 44 pins, through hole")
newPart.addTag("kicadTags", "plcc leaded")
newPart.addTag("kicadAttr", "through_hole")
newPart.addTag("kicad3DModel", "${KICAD6_3DMODEL_DIR}/Package_LCC.3dshapes/PLCC-44_THT-Socket.wrl")

OOMP.parts.append(newPart)