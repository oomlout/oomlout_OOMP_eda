###### OOMP FILE  ######

import OOMP

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "kicad")
newPart.addTag("oompColor", "kicad-footprints")
newPart.addTag("oompDesc", "OptoDevice")
newPart.addTag("oompIndex", "Kodenshi_SG105_Reverse")

newPart.addTag("kicadDesc", "package for Kodenshi SG-105 with PCB cutout, light-direction downwards, see http://www.kodenshi.co.jp/products/pdf/sensor/photointerrupter_ref/SG-105.pdf")
newPart.addTag("kicadTags", "refective opto couple photo coupler")
newPart.addTag("kicadAttr", "smd")
newPart.addTag("kicad3DModel", "${KICAD6_3DMODEL_DIR}/OptoDevice.3dshapes/Kodenshi_SG105_Reverse.wrl")

OOMP.parts.append(newPart)