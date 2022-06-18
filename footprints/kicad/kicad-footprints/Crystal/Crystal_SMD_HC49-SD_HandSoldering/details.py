###### OOMP FILE  ######

import OOMP

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "kicad")
newPart.addTag("oompColor", "kicad-footprints")
newPart.addTag("oompDesc", "Crystal")
newPart.addTag("oompIndex", "Crystal_SMD_HC49-SD_HandSoldering")

newPart.addTag("kicadDesc", "SMD Crystal HC-49-SD http://cdn-reichelt.de/documents/datenblatt/B400/xxx-HC49-SMD.pdf, hand-soldering, 11.4x4.7mm^2 package")
newPart.addTag("kicadTags", "SMD SMT crystal hand-soldering")
newPart.addTag("kicadAttr", "smd")
newPart.addTag("kicad3DModel", "${KICAD6_3DMODEL_DIR}/Crystal.3dshapes/Crystal_SMD_HC49-SD.wrl")

OOMP.parts.append(newPart)