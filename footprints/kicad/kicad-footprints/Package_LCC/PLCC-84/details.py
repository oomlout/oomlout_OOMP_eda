###### OOMP FILE  ######

import OOMP

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "kicad")
newPart.addTag("oompColor", "kicad-footprints")
newPart.addTag("oompDesc", "Package_LCC")
newPart.addTag("oompIndex", "PLCC-84")

newPart.addTag("kicadDesc", "PLCC, 84 pins, surface mount")
newPart.addTag("kicadTags", "plcc smt")
newPart.addTag("kicadAttr", "smd")
newPart.addTag("kicad3DModel", "${KICAD6_3DMODEL_DIR}/Package_LCC.3dshapes/PLCC-84.wrl")

OOMP.parts.append(newPart)