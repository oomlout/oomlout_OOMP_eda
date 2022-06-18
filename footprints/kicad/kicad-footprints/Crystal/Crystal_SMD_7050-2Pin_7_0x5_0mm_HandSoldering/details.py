###### OOMP FILE  ######

import OOMP

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "kicad")
newPart.addTag("oompColor", "kicad-footprints")
newPart.addTag("oompDesc", "Crystal")
newPart.addTag("oompIndex", "Crystal_SMD_7050-2Pin_7.0x5.0mm_HandSoldering")

newPart.addTag("kicadDesc", "SMD Crystal SERIES SMD7050/4 https://www.foxonline.com/pdfs/FQ7050.pdf, hand-soldering, 7.0x5.0mm^2 package")
newPart.addTag("kicadTags", "SMD SMT crystal hand-soldering")
newPart.addTag("kicadAttr", "smd")
newPart.addTag("kicad3DModel", "${KICAD6_3DMODEL_DIR}/Crystal.3dshapes/Crystal_SMD_7050-2Pin_7.0x5.0mm_HandSoldering.wrl")

OOMP.parts.append(newPart)