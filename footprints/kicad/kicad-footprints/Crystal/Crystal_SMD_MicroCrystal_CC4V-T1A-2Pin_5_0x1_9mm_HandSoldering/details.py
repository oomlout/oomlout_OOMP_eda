###### OOMP FILE  ######

import OOMP

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "kicad")
newPart.addTag("oompColor", "kicad-footprints")
newPart.addTag("oompDesc", "Crystal")
newPart.addTag("oompIndex", "Crystal_SMD_MicroCrystal_CC4V-T1A-2Pin_5.0x1.9mm_HandSoldering")

newPart.addTag("kicadDesc", "SMD Crystal MicroCrystal CC4V-T1A series http://cdn-reichelt.de/documents/datenblatt/B400/CC4V-T1A.pdf, hand-soldering, 5.0x1.9mm^2 package")
newPart.addTag("kicadTags", "SMD SMT crystal hand-soldering")
newPart.addTag("kicadAttr", "smd")
newPart.addTag("kicad3DModel", "${KICAD6_3DMODEL_DIR}/Crystal.3dshapes/Crystal_SMD_MicroCrystal_CC4V-T1A-2Pin_5.0x1.9mm_HandSoldering.wrl")

OOMP.parts.append(newPart)