###### OOMP FILE  ######

import OOMP

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "kicad")
newPart.addTag("oompColor", "kicad-footprints")
newPart.addTag("oompDesc", "Sensor_Distance")
newPart.addTag("oompIndex", "ST_VL53L1x")

newPart.addTag("kicadDesc", "VL53L1x distance sensor")
newPart.addTag("kicadTags", "VL53L1CXV0FY1 VL53L1x")
newPart.addTag("kicadAttr", "smd")
newPart.addTag("kicad3DModel", "${KICAD6_3DMODEL_DIR}/Sensor_Distance.3dshapes/ST_VL53L1x.wrl")

OOMP.parts.append(newPart)