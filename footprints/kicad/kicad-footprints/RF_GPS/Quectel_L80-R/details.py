###### OOMP FILE  ######

import OOMP

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "kicad")
newPart.addTag("oompColor", "kicad-footprints")
newPart.addTag("oompDesc", "RF_GPS")
newPart.addTag("oompIndex", "Quectel_L80-R")
newPart.addTag("oompName", "kicad-footprints/RF_GPS/Quectel_L80-R")

newPart.addTag("kicadDesc", "Quectel L80-R GPS Module, Patch on Top, https://www.quectel.com/UploadImage/Downlad/Quectel_L80-R_Hardware_Design_V1.2.pdf")
newPart.addTag("kicadTags", "quectel GPS GNSS")
newPart.addTag("kicadAttr", "smd")
newPart.addTag("kicad3DModel", "${KICAD6_3DMODEL_DIR}/RF_GPS.3dshapes/Quectel_L80-R.wrl")

OOMP.parts.append(newPart)