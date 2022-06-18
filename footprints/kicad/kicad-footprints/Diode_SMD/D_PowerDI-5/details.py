###### OOMP FILE  ######

import OOMP

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "kicad")
newPart.addTag("oompColor", "kicad-footprints")
newPart.addTag("oompDesc", "Diode_SMD")
newPart.addTag("oompIndex", "D_PowerDI-5")

newPart.addTag("kicadDesc", "PowerDI,Diode,Vishay,https://www.diodes.com/assets/Package-Files/PowerDI5.pdf")
newPart.addTag("kicadTags", "PowerDI diode vishay")
newPart.addTag("kicadAttr", "smd")
newPart.addTag("kicad3DModel", "${KICAD6_3DMODEL_DIR}/Diode_SMD.3dshapes/D_PowerDI-5.wrl")

OOMP.parts.append(newPart)