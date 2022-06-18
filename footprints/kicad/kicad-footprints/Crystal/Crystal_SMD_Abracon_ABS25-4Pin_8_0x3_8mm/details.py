###### OOMP FILE  ######

import OOMP

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "kicad")
newPart.addTag("oompColor", "kicad-footprints")
newPart.addTag("oompDesc", "Crystal")
newPart.addTag("oompIndex", "Crystal_SMD_Abracon_ABS25-4Pin_8.0x3.8mm")

newPart.addTag("kicadDesc", "Abracon Miniature Ceramic SMD Crystal ABS25 https://abracon.com/Resonators/abs25.pdf, 8.0x3.8mm^2 package")
newPart.addTag("kicadTags", "SMD SMT crystal")
newPart.addTag("kicadAttr", "smd")
newPart.addTag("kicad3DModel", "${KICAD6_3DMODEL_DIR}/Crystal.3dshapes/Crystal_SMD_Abracon_ABS25-4Pin_8.0x3.8mm.wrl")

OOMP.parts.append(newPart)