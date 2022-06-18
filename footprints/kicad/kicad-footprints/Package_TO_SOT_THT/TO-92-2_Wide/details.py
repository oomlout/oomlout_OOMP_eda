###### OOMP FILE  ######

import OOMP

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "kicad")
newPart.addTag("oompColor", "kicad-footprints")
newPart.addTag("oompDesc", "Package_TO_SOT_THT")
newPart.addTag("oompIndex", "TO-92-2_Wide")

newPart.addTag("kicadDesc", "TO-92 2-pin leads in-line, wide, drill 0.75mm")
newPart.addTag("kicadTags", "to-92 sc-43 sc-43a sot54 PA33 diode SOD70")
newPart.addTag("kicadAttr", "through_hole")
newPart.addTag("kicad3DModel", "${KICAD6_3DMODEL_DIR}/Package_TO_SOT_THT.3dshapes/TO-92-2_Wide.wrl")

OOMP.parts.append(newPart)