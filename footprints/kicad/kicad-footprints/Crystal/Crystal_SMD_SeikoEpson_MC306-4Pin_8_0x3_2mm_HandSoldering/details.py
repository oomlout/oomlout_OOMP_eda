###### OOMP FILE  ######

import OOMP

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "kicad")
newPart.addTag("oompColor", "kicad-footprints")
newPart.addTag("oompDesc", "Crystal")
newPart.addTag("oompIndex", "Crystal_SMD_SeikoEpson_MC306-4Pin_8.0x3.2mm_HandSoldering")

newPart.addTag("kicadDesc", "SMD Crystal Seiko Epson MC-306 https://support.epson.biz/td/api/doc_check.php?dl=brief_MC-306_en.pdf, hand-soldering, 8.0x3.2mm^2 package")
newPart.addTag("kicadTags", "SMD SMT crystal hand-soldering")
newPart.addTag("kicadAttr", "smd")
newPart.addTag("kicad3DModel", "${KICAD6_3DMODEL_DIR}/Crystal.3dshapes/Crystal_SMD_SeikoEpson_MC306-4Pin_8.0x3.2mm_HandSoldering.wrl")

OOMP.parts.append(newPart)