###### OOMP FILE  ######

import OOMP

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "kicad")
newPart.addTag("oompColor", "kicad-footprints")
newPart.addTag("oompDesc", "RF_GPS")
newPart.addTag("oompIndex", "SIM28ML")

newPart.addTag("kicadDesc", "https://simcom.ee/documents/SIM28ML/SIM28ML_Hardware%20Design_V1.01.pdf")
newPart.addTag("kicadTags", "SIM28ML GPS")
newPart.addTag("kicadAttr", "smd")
newPart.addTag("kicad3DModel", "${KICAD6_3DMODEL_DIR}/RF_GPS.3dshapes/SIM28ML.wrl")

OOMP.parts.append(newPart)