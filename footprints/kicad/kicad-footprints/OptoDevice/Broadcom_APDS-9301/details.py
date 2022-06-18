###### OOMP FILE  ######

import OOMP

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "kicad")
newPart.addTag("oompColor", "kicad-footprints")
newPart.addTag("oompDesc", "OptoDevice")
newPart.addTag("oompIndex", "Broadcom_APDS-9301")
newPart.addTag("oompName", "kicad-footprints/OptoDevice/Broadcom_APDS-9301")

newPart.addTag("kicadDesc", "ambient light sensor, i2c interface, 6-pin chipled package, https://docs.broadcom.com/docs/AV02-2315EN")
newPart.addTag("kicadTags", "ambient light sensor chipled")
newPart.addTag("kicadAttr", "smd")
newPart.addTag("kicad3DModel", "${KICAD6_3DMODEL_DIR}/OptoDevice.3dshapes/Broadcom_APDS-9301.wrl")

OOMP.parts.append(newPart)