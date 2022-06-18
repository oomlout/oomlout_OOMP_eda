###### OOMP FILE  ######

import OOMP

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "kicad")
newPart.addTag("oompColor", "kicad-footprints")
newPart.addTag("oompDesc", "Oscillator")
newPart.addTag("oompIndex", "Oscillator_SMD_IQD_IQXO70-4Pin_7.5x5.0mm")

newPart.addTag("kicadDesc", "IQD Crystal Clock Oscillator IQXO-70, http://www.iqdfrequencyproducts.com/products/details/iqxo-70-11-30.pdf, 7.5x5.0mm^2 package")
newPart.addTag("kicadTags", "SMD SMT crystal oscillator")
newPart.addTag("kicadAttr", "smd")
newPart.addTag("kicad3DModel", "${KICAD6_3DMODEL_DIR}/Oscillator.3dshapes/Oscillator_SMD_IQD_IQXO70-4Pin_7.5x5.0mm.wrl")

OOMP.parts.append(newPart)