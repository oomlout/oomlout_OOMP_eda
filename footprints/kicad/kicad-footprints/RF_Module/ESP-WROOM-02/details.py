###### OOMP FILE  ######

import OOMP

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "kicad")
newPart.addTag("oompColor", "kicad-footprints")
newPart.addTag("oompDesc", "RF_Module")
newPart.addTag("oompIndex", "ESP-WROOM-02")

newPart.addTag("kicadDesc", "https://www.espressif.com/sites/default/files/documentation/0c-esp-wroom-02_datasheet_en.pdf")
newPart.addTag("kicadTags", "ESP WROOM-02 espressif esp8266ex")
newPart.addTag("kicadAttr", "smd")
newPart.addTag("kicad3DModel", "${KICAD6_3DMODEL_DIR}/RF_Module.3dshapes/ESP-WROOM-02.wrl")

OOMP.parts.append(newPart)