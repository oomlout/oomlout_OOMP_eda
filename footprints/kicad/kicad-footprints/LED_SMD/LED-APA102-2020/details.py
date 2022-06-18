###### OOMP FILE  ######

import OOMP

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "kicad")
newPart.addTag("oompColor", "kicad-footprints")
newPart.addTag("oompDesc", "LED_SMD")
newPart.addTag("oompIndex", "LED-APA102-2020")
newPart.addTag("oompName", "kicad-footprints/LED_SMD/LED-APA102-2020")

newPart.addTag("kicadDesc", "http://www.led-color.com/upload/201604/APA102-2020%20SMD%20LED.pdf")
newPart.addTag("kicadTags", "LED RGB SPI")
newPart.addTag("kicadAttr", "smd")
newPart.addTag("kicad3DModel", "${KICAD6_3DMODEL_DIR}/LED_SMD.3dshapes/LED-APA102-2020.wrl")

OOMP.parts.append(newPart)