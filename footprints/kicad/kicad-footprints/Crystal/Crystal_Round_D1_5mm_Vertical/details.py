###### OOMP FILE  ######

import OOMP

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "kicad")
newPart.addTag("oompColor", "kicad-footprints")
newPart.addTag("oompDesc", "Crystal")
newPart.addTag("oompIndex", "Crystal_Round_D1.5mm_Vertical")

newPart.addTag("kicadDesc", "Crystal THT DS15 5.0mm length 1.5mm diameter http://www.microcrystal.com/images/_Product-Documentation/03_TF_metal_Packages/01_Datasheet/DS-Series.pdf")
newPart.addTag("kicadTags", "['DS15']")
newPart.addTag("kicadAttr", "through_hole")
newPart.addTag("kicad3DModel", "${KICAD6_3DMODEL_DIR}/Crystal.3dshapes/Crystal_Round_D1.5mm_Vertical.wrl")

OOMP.parts.append(newPart)