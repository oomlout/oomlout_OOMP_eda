###### OOMP FILE  ######

import OOMP

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "kicad")
newPart.addTag("oompColor", "kicad-footprints")
newPart.addTag("oompDesc", "Sensor")
newPart.addTag("oompIndex", "SHT1x")

newPart.addTag("kicadDesc", "SHT1x")
newPart.addTag("kicadTags", "SHT1x")
newPart.addTag("kicadAttr", "smd")
newPart.addTag("kicad3DModel", "${KICAD6_3DMODEL_DIR}/Sensor_Temperature.3dshapes/SHT1x.wrl")

OOMP.parts.append(newPart)