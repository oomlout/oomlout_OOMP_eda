###### OOMP FILE  ######

import OOMP

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "kicad")
newPart.addTag("oompColor", "kicad-footprints")
newPart.addTag("oompDesc", "OptoDevice")
newPart.addTag("oompIndex", "OnSemi_CASE100CY")
newPart.addTag("oompName", "kicad-footprints/OptoDevice/OnSemi_CASE100CY")

newPart.addTag("kicadDesc", "OnSemi CASE 100CY, light-direction upwards, see http://www.onsemi.com/pub/Collateral/QRE1113-D.PDF")
newPart.addTag("kicadTags", "refective opto couple photo coupler")
newPart.addTag("kicadAttr", "smd")
newPart.addTag("kicad3DModel", "${KICAD6_3DMODEL_DIR}/OptoDevice.3dshapes/OnSemi_CASE100CY.wrl")

OOMP.parts.append(newPart)