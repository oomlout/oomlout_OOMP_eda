###### OOMP FILE  ######

import OOMP

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "kicad")
newPart.addTag("oompColor", "kicad-footprints")
newPart.addTag("oompDesc", "Package_TO_SOT_THT")
newPart.addTag("oompIndex", "TO-218-3_Vertical")

newPart.addTag("kicadDesc", "TO-218-3, Vertical, RM 5.475mm, SOT-93, see https://www.vishay.com/docs/95214/fto218.pdf")
newPart.addTag("kicadTags", "TO-218-3 Vertical RM 5.475mm SOT-93")
newPart.addTag("kicadAttr", "through_hole")
newPart.addTag("kicad3DModel", "${KICAD6_3DMODEL_DIR}/Package_TO_SOT_THT.3dshapes/TO-218-3_Vertical.wrl")

OOMP.parts.append(newPart)