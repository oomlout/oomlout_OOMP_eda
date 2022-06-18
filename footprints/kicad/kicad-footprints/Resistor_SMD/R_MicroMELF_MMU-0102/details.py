###### OOMP FILE  ######

import OOMP

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "kicad")
newPart.addTag("oompColor", "kicad-footprints")
newPart.addTag("oompDesc", "Resistor_SMD")
newPart.addTag("oompIndex", "R_MicroMELF_MMU-0102")

newPart.addTag("kicadDesc", "Resistor, MicroMELF, MMU-0102, http://www.vishay.com/docs/28713/melfprof.pdf")
newPart.addTag("kicadTags", "MicroMELF Resistor")
newPart.addTag("kicadAttr", "smd")
newPart.addTag("kicad3DModel", "${KICAD6_3DMODEL_DIR}/Resistor_SMD.3dshapes/R_MicroMELF_MMU-0102.wrl")

OOMP.parts.append(newPart)