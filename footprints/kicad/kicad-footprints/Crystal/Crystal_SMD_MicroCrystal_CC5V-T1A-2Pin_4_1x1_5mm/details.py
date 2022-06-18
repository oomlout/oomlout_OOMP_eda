###### OOMP FILE  ######

import OOMP

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "kicad")
newPart.addTag("oompColor", "kicad-footprints")
newPart.addTag("oompDesc", "Crystal")
newPart.addTag("oompIndex", "Crystal_SMD_MicroCrystal_CC5V-T1A-2Pin_4.1x1.5mm")

newPart.addTag("kicadDesc", "SMD Crystal MicroCrystal CC5V-T1A series http://cdn-reichelt.de/documents/datenblatt/B400/CC5V-T1A.pdf, 4.1x1.5mm^2 package")
newPart.addTag("kicadTags", "SMD SMT crystal")
newPart.addTag("kicadAttr", "smd")
newPart.addTag("kicad3DModel", "${KICAD6_3DMODEL_DIR}/Crystal.3dshapes/Crystal_SMD_MicroCrystal_CC5V-T1A-2Pin_4.1x1.5mm.wrl")

OOMP.parts.append(newPart)