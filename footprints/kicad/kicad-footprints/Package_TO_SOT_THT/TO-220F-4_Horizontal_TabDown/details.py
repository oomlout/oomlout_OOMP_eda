###### OOMP FILE  ######

import OOMP

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "kicad")
newPart.addTag("oompColor", "kicad-footprints")
newPart.addTag("oompDesc", "Package_TO_SOT_THT")
newPart.addTag("oompIndex", "TO-220F-4_Horizontal_TabDown")

newPart.addTag("kicadDesc", "TO-220F-4, Horizontal, RM 2.54mm, see https://www.njr.com/semicon/PDF/package/TO-220F-4_E.pdf")
newPart.addTag("kicadTags", "TO-220F-4 Horizontal RM 2.54mm")
newPart.addTag("kicadAttr", "through_hole")
newPart.addTag("kicad3DModel", "${KICAD6_3DMODEL_DIR}/Package_TO_SOT_THT.3dshapes/TO-220F-4_Horizontal_TabDown.wrl")

OOMP.parts.append(newPart)