###### OOMP FILE  ######

import OOMP

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "kicad")
newPart.addTag("oompColor", "kicad-footprints")
newPart.addTag("oompDesc", "Package_TO_SOT_THT")
newPart.addTag("oompIndex", "TO-220F-2_Horizontal_TabDown")

newPart.addTag("kicadDesc", "TO-220F-2, Horizontal, RM 5.08mm, see http://www.onsemi.com/pub/Collateral/FFPF10F150S-D.pdf")
newPart.addTag("kicadTags", "TO-220F-2 Horizontal RM 5.08mm")
newPart.addTag("kicadAttr", "through_hole")
newPart.addTag("kicad3DModel", "${KICAD6_3DMODEL_DIR}/Package_TO_SOT_THT.3dshapes/TO-220F-2_Horizontal_TabDown.wrl")

OOMP.parts.append(newPart)