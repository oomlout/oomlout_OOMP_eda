###### OOMP FILE  ######

import OOMP

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "kicad")
newPart.addTag("oompColor", "kicad-footprints")
newPart.addTag("oompDesc", "Crystal")
newPart.addTag("oompIndex", "Resonator_SMD_Murata_CDSCB-2Pin_4.5x2.0mm_HandSoldering")

newPart.addTag("kicadDesc", "SMD Resomator/Filter Murata CDSCB, http://cdn-reichelt.de/documents/datenblatt/B400/SFECV-107.pdf, hand-soldering, 4.5x2.0mm^2 package")
newPart.addTag("kicadTags", "SMD SMT ceramic resonator filter filter hand-soldering")
newPart.addTag("kicadAttr", "smd")
newPart.addTag("kicad3DModel", "${KICAD6_3DMODEL_DIR}/Crystal.3dshapes/Resonator_SMD_Murata_CDSCB-2Pin_4.5x2.0mm.wrl")

OOMP.parts.append(newPart)