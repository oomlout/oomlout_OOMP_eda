###### OOMP FILE  ######

import OOMP

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "kicad")
newPart.addTag("oompColor", "kicad-footprints")
newPart.addTag("oompDesc", "RF_Module")
newPart.addTag("oompIndex", "ESP32-S2-MINI-1U")

newPart.addTag("kicadDesc", "2.4 GHz Wi-Fi and Bluetooth combo chip, external antenna, https://www.espressif.com/sites/default/files/documentation/esp32-s3-mini-1_mini-1u_datasheet_en.pdf")
newPart.addTag("kicadTags", "2.4 GHz Wi-Fi Bluetooth external antenna espressif  15.4*15.4mm")
newPart.addTag("kicadAttr", "smd")
newPart.addTag("kicad3DModel", "${KICAD6_3DMODEL_DIR}/RF_Module.3dshapes/ESP32-S2-MINI-1U.wrl")

OOMP.parts.append(newPart)