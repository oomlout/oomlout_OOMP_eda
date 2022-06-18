###### OOMP FILE  ######

import OOMP

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "kicad")
newPart.addTag("oompColor", "kicad-footprints")
newPart.addTag("oompDesc", "OptoDevice")
newPart.addTag("oompIndex", "Kodenshi_SG105")
newPart.addTag("oompName", "kicad-footprints/OptoDevice/Kodenshi_SG105")

newPart.addTag("kicadDesc", "package for Kodenshi SG-105 with PCB cutout, light-direction upwards, see http://www.kodenshi.co.jp/products/pdf/sensor/photointerrupter_ref/SG-105.pdf")
newPart.addTag("kicadTags", "refective opto couple photo coupler")
newPart.addTag("kicadAttr", "smd")
newPart.addTag("kicad3DModel", "${KICAD6_3DMODEL_DIR}/OptoDevice.3dshapes/Kodenshi_SG105.wrl")

OOMP.parts.append(newPart)