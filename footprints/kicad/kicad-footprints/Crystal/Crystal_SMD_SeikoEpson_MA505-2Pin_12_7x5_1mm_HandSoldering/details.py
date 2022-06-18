###### OOMP FILE  ######

import OOMP

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "kicad")
newPart.addTag("oompColor", "kicad-footprints")
newPart.addTag("oompDesc", "Crystal")
newPart.addTag("oompIndex", "Crystal_SMD_SeikoEpson_MA505-2Pin_12.7x5.1mm_HandSoldering")

newPart.addTag("kicadDesc", "SMD Crystal Seiko Epson MC-505 http://media.digikey.com/pdf/Data%20Sheets/Epson%20PDFs/MA-505,506.pdf, hand-soldering, 12.7x5.1mm^2 package")
newPart.addTag("kicadTags", "SMD SMT crystal hand-soldering")
newPart.addTag("kicadAttr", "smd")
newPart.addTag("kicad3DModel", "${KICAD6_3DMODEL_DIR}/Crystal.3dshapes/Crystal_SMD_SeikoEpson_MA505-2Pin_12.7x5.1mm_HandSoldering.wrl")

OOMP.parts.append(newPart)