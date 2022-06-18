###### OOMP FILE  ######

import OOMP

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "kicad")
newPart.addTag("oompColor", "kicad-footprints")
newPart.addTag("oompDesc", "Package_SON")
newPart.addTag("oompIndex", "Texas_DRC0010J_ThermalVias")

newPart.addTag("kicadDesc", "Texas DRC0010J, VSON10 3x3mm Body, 0.5mm Pitch,  http://www.ti.com/lit/ds/symlink/tps63000.pdf")
newPart.addTag("kicadTags", "Texas VSON10 3x3mm")
newPart.addTag("kicadAttr", "smd")
newPart.addTag("kicad3DModel", "${KICAD6_3DMODEL_DIR}/Package_SON.3dshapes/Texas_DRC0010J.wrl")

OOMP.parts.append(newPart)