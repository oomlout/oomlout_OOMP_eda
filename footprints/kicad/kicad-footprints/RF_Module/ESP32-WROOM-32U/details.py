###### OOMP FILE  ######

import OOMP

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "kicad")
newPart.addTag("oompColor", "kicad-footprints")
newPart.addTag("oompDesc", "RF_Module")
newPart.addTag("oompIndex", "ESP32-WROOM-32U")

newPart.addTag("kicadDesc", "Single 2.4 GHz Wi-Fi and Bluetooth combo chip with U.FL connector, https://www.espressif.com/sites/default/files/documentation/esp32-wroom-32d_esp32-wroom-32u_datasheet_en.pdf")
newPart.addTag("kicadTags", "Single 2.4 GHz Wi-Fi and Bluetooth combo  chip")
newPart.addTag("kicadAttr", "smd")
newPart.addTag("kicad3DModel", "${KICAD6_3DMODEL_DIR}/RF_Module.3dshapes/ESP32-WROOM-32U.wrl")

OOMP.parts.append(newPart)