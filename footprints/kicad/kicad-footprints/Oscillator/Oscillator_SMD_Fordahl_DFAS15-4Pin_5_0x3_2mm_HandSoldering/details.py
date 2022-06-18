###### OOMP FILE  ######

import OOMP

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "kicad")
newPart.addTag("oompColor", "kicad-footprints")
newPart.addTag("oompDesc", "Oscillator")
newPart.addTag("oompIndex", "Oscillator_SMD_Fordahl_DFAS15-4Pin_5.0x3.2mm_HandSoldering")

newPart.addTag("kicadDesc", "Ultraminiature Crystal Clock Oscillator TXCO Fordahl DFA S15-OV/UOV, http://www.iqdfrequencyproducts.com/products/details/iqxo-70-11-30.pdf, hand-soldering, 5.0x3.2mm^2 package")
newPart.addTag("kicadTags", "SMD SMT crystal oscillator hand-soldering")
newPart.addTag("kicadAttr", "smd")
newPart.addTag("kicad3DModel", "${KICAD6_3DMODEL_DIR}/Oscillator.3dshapes/Oscillator_SMD_Fordahl_DFAS15-4Pin_5.0x3.2mm_HandSoldering.wrl")

OOMP.parts.append(newPart)