###### OOMP FILE  ######

import OOMP

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "kicad")
newPart.addTag("oompColor", "kicad-footprints")
newPart.addTag("oompDesc", "Diode_SMD")
newPart.addTag("oompIndex", "D_MicroMELF_Handsoldering")

newPart.addTag("kicadDesc", "Diode, MicroMELF, Hand Soldering, http://www.vishay.com/docs/85597/bzm55.pdf")
newPart.addTag("kicadTags", "MicroMELF Diode")
newPart.addTag("kicadAttr", "smd")
newPart.addTag("kicad3DModel", "${KICAD6_3DMODEL_DIR}/Diode_SMD.3dshapes/D_MicroMELF.wrl")

OOMP.parts.append(newPart)