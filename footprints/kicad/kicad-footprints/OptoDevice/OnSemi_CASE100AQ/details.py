###### OOMP FILE  ######

import OOMP

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "kicad")
newPart.addTag("oompColor", "kicad-footprints")
newPart.addTag("oompDesc", "OptoDevice")
newPart.addTag("oompIndex", "OnSemi_CASE100AQ")

newPart.addTag("kicadDesc", "OnSemi CASE 100AQ for QRE1113, see https://www.onsemi.com/pub/Collateral/QRE1113-D.PDF")
newPart.addTag("kicadTags", "reflective opto couple photo coupler")
newPart.addTag("kicadAttr", "through_hole")
newPart.addTag("kicad3DModel", "${KICAD6_3DMODEL_DIR}/OptoDevice.3dshapes/OnSemi_CASE100AQ.wrl")

OOMP.parts.append(newPart)