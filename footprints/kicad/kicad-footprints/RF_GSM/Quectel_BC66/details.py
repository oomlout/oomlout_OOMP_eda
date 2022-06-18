###### OOMP FILE  ######

import OOMP

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "kicad")
newPart.addTag("oompColor", "kicad-footprints")
newPart.addTag("oompDesc", "RF_GSM")
newPart.addTag("oompIndex", "Quectel_BC66")

newPart.addTag("kicadDesc", "GSM NB-IoT module, 15.8x17.7x2mm, https://www.quectel.com/UploadImage/Downlad/Quectel_BC66_Hardware_Design_V1.1.pdf")
newPart.addTag("kicadTags", "GSM NB-IoT Module BC66 M66")
newPart.addTag("kicadAttr", "smd")
newPart.addTag("kicad3DModel", "${KICAD6_3DMODEL_DIR}/RF_GSM.3dshapes/Quectel_BC66.wrl")

OOMP.parts.append(newPart)