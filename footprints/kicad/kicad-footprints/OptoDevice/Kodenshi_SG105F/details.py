###### OOMP FILE  ######

import OOMP

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "kicad")
newPart.addTag("oompColor", "kicad-footprints")
newPart.addTag("oompDesc", "OptoDevice")
newPart.addTag("oompIndex", "Kodenshi_SG105F")

newPart.addTag("kicadDesc", "package for Kodenshi SG-105F, see http://www.kodenshi.co.jp/products/pdf/sensor/photointerrupter_ref/SG-105F.pdf")
newPart.addTag("kicadTags", "refective opto couple photo coupler")
newPart.addTag("kicadAttr", "through_hole")
newPart.addTag("kicad3DModel", "${KICAD6_3DMODEL_DIR}/OptoDevice.3dshapes/Kodenshi_SG105F.wrl")

OOMP.parts.append(newPart)