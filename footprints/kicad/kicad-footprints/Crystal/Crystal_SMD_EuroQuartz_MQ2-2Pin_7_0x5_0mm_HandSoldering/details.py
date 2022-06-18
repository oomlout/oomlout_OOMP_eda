###### OOMP FILE  ######

import OOMP

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "kicad")
newPart.addTag("oompColor", "kicad-footprints")
newPart.addTag("oompDesc", "Crystal")
newPart.addTag("oompIndex", "Crystal_SMD_EuroQuartz_MQ2-2Pin_7.0x5.0mm_HandSoldering")

newPart.addTag("kicadDesc", "SMD Crystal EuroQuartz MQ2 series http://cdn-reichelt.de/documents/datenblatt/B400/MQ.pdf, hand-soldering, 7.0x5.0mm^2 package")
newPart.addTag("kicadTags", "SMD SMT crystal hand-soldering")
newPart.addTag("kicadAttr", "smd")
newPart.addTag("kicad3DModel", "${KICAD6_3DMODEL_DIR}/Crystal.3dshapes/Crystal_SMD_EuroQuartz_MQ2-2Pin_7.0x5.0mm_HandSoldering.wrl")

OOMP.parts.append(newPart)