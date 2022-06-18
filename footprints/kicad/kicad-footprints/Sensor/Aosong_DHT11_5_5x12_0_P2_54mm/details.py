###### OOMP FILE  ######

import OOMP

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "kicad")
newPart.addTag("oompColor", "kicad-footprints")
newPart.addTag("oompDesc", "Sensor")
newPart.addTag("oompIndex", "Aosong_DHT11_5.5x12.0_P2.54mm")

newPart.addTag("kicadDesc", "Temperature and humidity module, http://akizukidenshi.com/download/ds/aosong/DHT11.pdf")
newPart.addTag("kicadTags", "Temperature and humidity module")
newPart.addTag("kicadAttr", "through_hole")
newPart.addTag("kicad3DModel", "${KICAD6_3DMODEL_DIR}/Sensor.3dshapes/Aosong_DHT11_5.5x12.0_P2.54mm.wrl")

OOMP.parts.append(newPart)