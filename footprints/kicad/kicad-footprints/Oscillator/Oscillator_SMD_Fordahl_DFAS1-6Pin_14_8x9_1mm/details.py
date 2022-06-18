###### OOMP FILE  ######

import OOMP

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "kicad")
newPart.addTag("oompColor", "kicad-footprints")
newPart.addTag("oompDesc", "Oscillator")
newPart.addTag("oompIndex", "Oscillator_SMD_Fordahl_DFAS1-6Pin_14.8x9.1mm")

newPart.addTag("kicadDesc", "Miniature Crystal Clock Oscillator TXCO Fordahl DFA S1-KHZ/LHZ, http://www.iqdfrequencyproducts.com/products/details/iqxo-70-11-30.pdf, 14.8x9.1mm^2 package")
newPart.addTag("kicadTags", "SMD SMT crystal oscillator")
newPart.addTag("kicadAttr", "smd")
newPart.addTag("kicad3DModel", "${KICAD6_3DMODEL_DIR}/Oscillator.3dshapes/Oscillator_SMD_Fordahl_DFAS1-6Pin_14.8x9.1mm.wrl")

OOMP.parts.append(newPart)