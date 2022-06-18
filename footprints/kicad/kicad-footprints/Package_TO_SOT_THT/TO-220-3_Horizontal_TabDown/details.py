###### OOMP FILE  ######

import OOMP

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "kicad")
newPart.addTag("oompColor", "kicad-footprints")
newPart.addTag("oompDesc", "Package_TO_SOT_THT")
newPart.addTag("oompIndex", "TO-220-3_Horizontal_TabDown")

newPart.addTag("kicadDesc", "TO-220-3, Horizontal, RM 2.54mm, see https://www.vishay.com/docs/66542/to-220-1.pdf")
newPart.addTag("kicadTags", "TO-220-3 Horizontal RM 2.54mm")
newPart.addTag("kicadAttr", "through_hole")
newPart.addTag("kicad3DModel", "${KICAD6_3DMODEL_DIR}/Package_TO_SOT_THT.3dshapes/TO-220-3_Horizontal_TabDown.wrl")

OOMP.parts.append(newPart)