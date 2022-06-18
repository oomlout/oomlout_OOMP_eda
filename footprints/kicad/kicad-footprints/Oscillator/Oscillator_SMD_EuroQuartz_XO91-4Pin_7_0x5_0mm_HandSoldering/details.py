###### OOMP FILE  ######

import OOMP

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "kicad")
newPart.addTag("oompColor", "kicad-footprints")
newPart.addTag("oompDesc", "Oscillator")
newPart.addTag("oompIndex", "Oscillator_SMD_EuroQuartz_XO91-4Pin_7.0x5.0mm_HandSoldering")

newPart.addTag("kicadDesc", "Miniature Crystal Clock Oscillator EuroQuartz XO91 series, http://cdn-reichelt.de/documents/datenblatt/B400/XO91.pdf, hand-soldering, 7.0x5.0mm^2 package")
newPart.addTag("kicadTags", "SMD SMT crystal oscillator hand-soldering")
newPart.addTag("kicadAttr", "smd")
newPart.addTag("kicad3DModel", "${KICAD6_3DMODEL_DIR}/Oscillator.3dshapes/Oscillator_SMD_EuroQuartz_XO91-4Pin_7.0x5.0mm_HandSoldering.wrl")

OOMP.parts.append(newPart)