###### OOMP FILE  ######

import OOMP

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "kicad")
newPart.addTag("oompColor", "kicad-footprints")
newPart.addTag("oompDesc", "OptoDevice")
newPart.addTag("oompIndex", "Broadcom_AFBR-16xxZ_Horizontal")

newPart.addTag("kicadDesc", "Fiber Optic Transmitter and Receiver, https://docs.broadcom.com/docs/AV02-4369EN")
newPart.addTag("kicadTags", "Fiber Optic Transmitter and Receiver")
newPart.addTag("kicadAttr", "through_hole")
newPart.addTag("kicad3DModel", "${KICAD6_3DMODEL_DIR}/OptoDevice.3dshapes/Broadcom_AFBR-16xxZ_Horizontal.wrl")

OOMP.parts.append(newPart)