###### OOMP FILE  ######

import OOMP

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "kicad")
newPart.addTag("oompColor", "kicad-footprints")
newPart.addTag("oompDesc", "OptoDevice")
newPart.addTag("oompIndex", "AGILENT_HFBR-152x")

newPart.addTag("kicadDesc", "Fiberoptic Transmitter TX, HFBR series (https://docs.broadcom.com/docs/AV02-3283EN)")
newPart.addTag("kicadTags", "Fiberoptic Transmitter")
newPart.addTag("kicadAttr", "through_hole")
newPart.addTag("kicad3DModel", "${KICAD6_3DMODEL_DIR}/OptoDevice.3dshapes/AGILENT_HFBR-152x.wrl")

OOMP.parts.append(newPart)