###### OOMP FILE  ######

import OOMP

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "kicad")
newPart.addTag("oompColor", "kicad-footprints")
newPart.addTag("oompDesc", "OptoDevice")
newPart.addTag("oompIndex", "Vishay_MOLD-3Pin")

newPart.addTag("kicadDesc", "IR Receiver Vishay TSOP-xxxx, MOLD package, see https://www.vishay.com/docs/82669/tsop32s40f.pdf")
newPart.addTag("kicadTags", "IR Receiver Vishay TSOP-xxxx MOLD")
newPart.addTag("kicadAttr", "through_hole")
newPart.addTag("kicad3DModel", "${KICAD6_3DMODEL_DIR}/OptoDevice.3dshapes/Vishay_MOLD-3Pin.wrl")

OOMP.parts.append(newPart)