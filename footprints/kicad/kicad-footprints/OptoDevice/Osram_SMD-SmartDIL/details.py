###### OOMP FILE  ######

import OOMP

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "kicad")
newPart.addTag("oompColor", "kicad-footprints")
newPart.addTag("oompDesc", "OptoDevice")
newPart.addTag("oompIndex", "Osram_SMD-SmartDIL")

newPart.addTag("kicadDesc", "PhotoDiode, plastic SMD SmatDIL")
newPart.addTag("kicadTags", "PhotoDiode plastic SMD SmatDIL")
newPart.addTag("kicadAttr", "smd")
newPart.addTag("kicad3DModel", "${KICAD6_3DMODEL_DIR}/OptoDevice.3dshapes/Osram_SMD-SmartDIL.wrl")

OOMP.parts.append(newPart)