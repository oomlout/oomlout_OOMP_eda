###### OOMP FILE  ######

import OOMP

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "kicad")
newPart.addTag("oompColor", "kicad-footprints")
newPart.addTag("oompDesc", "RF_GSM")
newPart.addTag("oompIndex", "SIMCom_SIM800C")

newPart.addTag("kicadDesc", "Quad-Band GSM/GPRS module, 17.6x15.7x2.3mm, http://simcom.ee/documents/SIM800C/SIM800C_Hardware_Design_V1.05.pdf")
newPart.addTag("kicadTags", "GSM Module SIM800C")
newPart.addTag("kicadAttr", "smd")
newPart.addTag("kicad3DModel", "${KICAD6_3DMODEL_DIR}/RF_GSM.3dshapes/SIMCom_SIM800C.wrl")

OOMP.parts.append(newPart)