###### OOMP FILE  ######

import OOMP

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "kicad")
newPart.addTag("oompColor", "kicad-footprints")
newPart.addTag("oompDesc", "Crystal")
newPart.addTag("oompIndex", "Resonator_SMD_Murata_SFSKA-3Pin_7.9x3.8mm_HandSoldering")

newPart.addTag("kicadDesc", "SMD Resomator/Filter Murata SFSKA, http://cdn-reichelt.de/documents/datenblatt/B400/SFECV-107.pdf, hand-soldering, 7.9x3.8mm^2 package")
newPart.addTag("kicadTags", "SMD SMT ceramic resonator filter filter hand-soldering")
newPart.addTag("kicadAttr", "smd")
newPart.addTag("kicad3DModel", "${KICAD6_3DMODEL_DIR}/Crystal.3dshapes/Resonator_SMD_Murata_SFSKA-3Pin_7.9x3.8mm_HandSoldering.wrl")

OOMP.parts.append(newPart)