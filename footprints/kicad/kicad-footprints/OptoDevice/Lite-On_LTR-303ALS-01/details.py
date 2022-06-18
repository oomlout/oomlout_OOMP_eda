###### OOMP FILE  ######

import OOMP

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "kicad")
newPart.addTag("oompColor", "kicad-footprints")
newPart.addTag("oompDesc", "OptoDevice")
newPart.addTag("oompIndex", "Lite-On_LTR-303ALS-01")

newPart.addTag("kicadDesc", "ambient light sensor, i2c interface, 6-pin chipled package, http://optoelectronics.liteon.com/upload/download/DS86-2013-0004/LTR-303ALS-01_DS_V1.pdf")
newPart.addTag("kicadTags", "ambient light sensor chipled")
newPart.addTag("kicadAttr", "smd")
newPart.addTag("kicad3DModel", "${KICAD6_3DMODEL_DIR}/OptoDevice.3dshapes/Lite-On_LTR-303ALS-01.wrl")

OOMP.parts.append(newPart)