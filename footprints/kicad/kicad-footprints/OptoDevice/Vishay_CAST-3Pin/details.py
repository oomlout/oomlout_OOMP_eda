###### OOMP FILE  ######

import OOMP

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "kicad")
newPart.addTag("oompColor", "kicad-footprints")
newPart.addTag("oompDesc", "OptoDevice")
newPart.addTag("oompIndex", "Vishay_CAST-3Pin")
newPart.addTag("oompName", "kicad-footprints/OptoDevice/Vishay_CAST-3Pin")

newPart.addTag("kicadDesc", "IR Receiver Vishay TSOP-xxxx, CAST package, see https://www.vishay.com/docs/82493/tsop311.pdf")
newPart.addTag("kicadTags", "IRReceiverVishayTSOP-xxxx CAST")
newPart.addTag("kicadAttr", "through_hole")
newPart.addTag("kicad3DModel", "${KICAD6_3DMODEL_DIR}/OptoDevice.3dshapes/Vishay_CAST-3Pin.wrl")

OOMP.parts.append(newPart)