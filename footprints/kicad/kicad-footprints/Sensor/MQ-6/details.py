###### OOMP FILE  ######

import OOMP

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "kicad")
newPart.addTag("oompColor", "kicad-footprints")
newPart.addTag("oompDesc", "Sensor")
newPart.addTag("oompIndex", "MQ-6")

newPart.addTag("kicadDesc", "Gas Sensor, 6 pin, https://www.winsen-sensor.com/d/files/semiconductor/mq-6.pdf")
newPart.addTag("kicadTags", "gas sensor")
newPart.addTag("kicadAttr", "through_hole")
newPart.addTag("kicad3DModel", "${KICAD6_3DMODEL_DIR}/Sensor.3dshapes/MQ-6.wrl")

OOMP.parts.append(newPart)