###### OOMP FILE  ######

import OOMP

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "kicad")
newPart.addTag("oompColor", "kicad-footprints")
newPart.addTag("oompDesc", "Diode_SMD")
newPart.addTag("oompIndex", "D_PowerDI-123")

newPart.addTag("kicadDesc", "http://www.diodes.com/_files/datasheets/ds30497.pdf")
newPart.addTag("kicadTags", "PowerDI diode vishay")
newPart.addTag("kicadAttr", "smd")
newPart.addTag("kicad3DModel", "${KICAD6_3DMODEL_DIR}/Diode_SMD.3dshapes/D_PowerDI-123.wrl")

OOMP.parts.append(newPart)