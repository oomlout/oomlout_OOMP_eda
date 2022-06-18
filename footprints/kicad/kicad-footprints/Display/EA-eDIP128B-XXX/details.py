###### OOMP FILE  ######

import OOMP

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "kicad")
newPart.addTag("oompColor", "kicad-footprints")
newPart.addTag("oompDesc", "Display")
newPart.addTag("oompIndex", "EA-eDIP128B-XXX")

newPart.addTag("kicadDesc", "LCD-graphical display with LED backlight 128x64 RS-232 I2C or SPI http://www.lcd-module.com/fileadmin/eng/pdf/grafik/edip128-6e.pdf")
newPart.addTag("kicadTags", "LCD-graphical display with LED backlight 128x64 RS-232 I2C or SPI")
newPart.addTag("kicadAttr", "through_hole")
newPart.addTag("kicad3DModel", "${KICAD6_3DMODEL_DIR}/Display.3dshapes/EA-eDIP128B-XXX.wrl")

OOMP.parts.append(newPart)