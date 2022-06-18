###### OOMP FILE  ######

import OOMP

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "kicad")
newPart.addTag("oompColor", "kicad-footprints")
newPart.addTag("oompDesc", "RF_Module")
newPart.addTag("oompIndex", "MOD-nRF8001")

newPart.addTag("kicadDesc", "BLE module, https://www.olimex.com/Products/Modules/RF/MOD-nRF8001/")
newPart.addTag("kicadTags", "BLE module")
newPart.addTag("kicadAttr", "smd")
newPart.addTag("kicad3DModel", "${KICAD6_3DMODEL_DIR}/RF_Module.3dshapes/MOD-nRF8001.wrl")

OOMP.parts.append(newPart)