###### OOMP FILE  ######

import OOMP

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "kicad")
newPart.addTag("oompColor", "kicad-footprints")
newPart.addTag("oompDesc", "Package_TO_SOT_THT")
newPart.addTag("oompIndex", "TO-92_HandSolder")

newPart.addTag("kicadDesc", "TO-92 leads molded, narrow, drill 0.75mm, handsoldering variant with enlarged pads (see NXP sot054_po.pdf)")
newPart.addTag("kicadTags", "to-92 sc-43 sc-43a sot54 PA33 transistor")
newPart.addTag("kicadAttr", "through_hole")
newPart.addTag("kicad3DModel", "${KICAD6_3DMODEL_DIR}/Package_TO_SOT_THT.3dshapes/TO-92.wrl")

OOMP.parts.append(newPart)