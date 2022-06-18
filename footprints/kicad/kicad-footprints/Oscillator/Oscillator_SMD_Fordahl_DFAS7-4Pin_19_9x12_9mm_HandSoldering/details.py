###### OOMP FILE  ######

import OOMP

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "kicad")
newPart.addTag("oompColor", "kicad-footprints")
newPart.addTag("oompDesc", "Oscillator")
newPart.addTag("oompIndex", "Oscillator_SMD_Fordahl_DFAS7-4Pin_19.9x12.9mm_HandSoldering")

newPart.addTag("kicadDesc", "Miniature Crystal Clock Oscillator TXCO Fordahl DFA S7-K/L, http://www.iqdfrequencyproducts.com/products/details/iqxo-70-11-30.pdf, hand-soldering, 19.9x12.9mm^2 package")
newPart.addTag("kicadTags", "SMD SMT crystal oscillator hand-soldering")
newPart.addTag("kicadAttr", "smd")
newPart.addTag("kicad3DModel", "${KICAD6_3DMODEL_DIR}/Oscillator.3dshapes/Oscillator_SMD_Fordahl_DFAS7-4Pin_19.9x12.9mm_HandSoldering.wrl")

OOMP.parts.append(newPart)