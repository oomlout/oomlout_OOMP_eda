###### OOMP FILE  ######

import OOMP

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "kicad")
newPart.addTag("oompColor", "kicad-footprints")
newPart.addTag("oompDesc", "Sensor")
newPart.addTag("oompIndex", "Senseair_S8_Up")

newPart.addTag("kicadDesc", "Sensair S8 Series CO2 sensor, 1kHz PWM output, Modbus, THT")
newPart.addTag("kicadTags", "co2 gas sensor pwm modbus")
newPart.addTag("kicadAttr", "through_hole")
newPart.addTag("kicad3DModel", "${KICAD6_3DMODEL_DIR}/Sensor.3dshapes/Senseair_S8_Up.wrl")

OOMP.parts.append(newPart)