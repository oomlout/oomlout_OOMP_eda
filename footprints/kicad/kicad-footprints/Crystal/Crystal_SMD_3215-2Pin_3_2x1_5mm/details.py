###### OOMP FILE  ######

import OOMP

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "kicad")
newPart.addTag("oompColor", "kicad-footprints")
newPart.addTag("oompDesc", "Crystal")
newPart.addTag("oompIndex", "Crystal_SMD_3215-2Pin_3.2x1.5mm")

newPart.addTag("kicadDesc", "SMD Crystal FC-135 https://support.epson.biz/td/api/doc_check.php?dl=brief_FC-135R_en.pdf")
newPart.addTag("kicadTags", "SMD SMT Crystal")
newPart.addTag("kicadAttr", "smd")
newPart.addTag("kicad3DModel", "${KICAD6_3DMODEL_DIR}/Crystal.3dshapes/Crystal_SMD_3215-2Pin_3.2x1.5mm.wrl")

OOMP.parts.append(newPart)