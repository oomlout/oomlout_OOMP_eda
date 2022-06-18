###### OOMP FILE  ######

import OOMP

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "kicad")
newPart.addTag("oompColor", "kicad-footprints")
newPart.addTag("oompDesc", "RF_GSM")
newPart.addTag("oompIndex", "SIMCom_SIM900")

newPart.addTag("kicadDesc", "Quad-Band GSM/GPRS module, 24x24x3mm, http://simcom.ee/documents/SIM900/SIM900_Hardware%20Design_V2.05.pdf")
newPart.addTag("kicadTags", "GSM Module SIM900")
newPart.addTag("kicadAttr", "smd")
newPart.addTag("kicad3DModel", "${KICAD6_3DMODEL_DIR}/RF_GSM.3dshapes/SIMCom_SIM900.wrl")

OOMP.parts.append(newPart)