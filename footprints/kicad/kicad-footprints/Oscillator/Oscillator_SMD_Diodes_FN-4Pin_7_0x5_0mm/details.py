###### OOMP FILE  ######

import OOMP

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "kicad")
newPart.addTag("oompColor", "kicad-footprints")
newPart.addTag("oompDesc", "Oscillator")
newPart.addTag("oompIndex", "Oscillator_SMD_Diodes_FN-4Pin_7.0x5.0mm")

newPart.addTag("kicadDesc", "FN Series Crystal Clock Oscillator (XO) (https://www.diodes.com/assets/Datasheets/FN_3-3V.pdf)")
newPart.addTag("kicadTags", "Oscillator Crystal SMD SMT")
newPart.addTag("kicadAttr", "smd")
newPart.addTag("kicad3DModel", "${KICAD6_3DMODEL_DIR}/Oscillator.3dshapes/Oscillator_SMD_Diodes_FN-4Pin_7.0x5.0mm.wrl")

OOMP.parts.append(newPart)