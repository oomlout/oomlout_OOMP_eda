###### OOMP FILE  ######

import OOMP

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "kicad")
newPart.addTag("oompColor", "kicad-footprints")
newPart.addTag("oompDesc", "OptoDevice")
newPart.addTag("oompIndex", "ST_VL53L0X")

newPart.addTag("kicadDesc", "https://www.st.com/resource/en/datasheet/vl53l1x.pdf")
newPart.addTag("kicadTags", "laser-ranging sensor")
newPart.addTag("kicadAttr", "smd")
newPart.addTag("kicad3DModel", "${KICAD6_3DMODEL_DIR}/OptoDevice.3dshapes/ST_VL53L0X.wrl")

OOMP.parts.append(newPart)