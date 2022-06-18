###### OOMP FILE  ######

import OOMP

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "kicad")
newPart.addTag("oompColor", "kicad-footprints")
newPart.addTag("oompDesc", "Display")
newPart.addTag("oompIndex", "Adafruit_SSD1306")

newPart.addTag("kicadDesc", "Adafruit SSD1306 OLED 1.3 inch 128x64 I2C & SPI https://learn.adafruit.com/monochrome-oled-breakouts/downloads")
newPart.addTag("kicadTags", "Adafruit SSD1306 OLED 1.3 inch 128x64 I2C & SPI")
newPart.addTag("kicadAttr", "through_hole")
newPart.addTag("kicad3DModel", "${KICAD6_3DMODEL_DIR}/Display.3dshapes/Adafruit_SSD1306.wrl")

OOMP.parts.append(newPart)