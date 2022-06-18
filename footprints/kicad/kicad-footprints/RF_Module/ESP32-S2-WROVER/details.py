###### OOMP FILE  ######

import OOMP

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "kicad")
newPart.addTag("oompColor", "kicad-footprints")
newPart.addTag("oompDesc", "RF_Module")
newPart.addTag("oompIndex", "ESP32-S2-WROVER")

newPart.addTag("kicadDesc", "ESP32-S2-WROVER(-I) 2.4 GHz Wi-Fi https://www.espressif.com/sites/default/files/documentation/esp32-s2-wroom_esp32-s2-wroom-i_datasheet_en.pdf")
newPart.addTag("kicadTags", "ESP32-S2  ESP32  WIFI")
newPart.addTag("kicadAttr", "smd")
newPart.addTag("kicad3DModel", "${KICAD6_3DMODEL_DIR}/RF_Module.3dshapes/ESP32-S2-WROVER.wrl")

OOMP.parts.append(newPart)