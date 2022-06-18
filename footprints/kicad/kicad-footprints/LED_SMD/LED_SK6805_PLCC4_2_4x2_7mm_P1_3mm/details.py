###### OOMP FILE  ######

import OOMP

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "kicad")
newPart.addTag("oompColor", "kicad-footprints")
newPart.addTag("oompDesc", "LED_SMD")
newPart.addTag("oompIndex", "LED_SK6805_PLCC4_2.4x2.7mm_P1.3mm")

newPart.addTag("kicadDesc", "https://cdn-shop.adafruit.com/product-files/3484/3484_Datasheet.pdf")
newPart.addTag("kicadTags", "LED RGB NeoPixel Nano")
newPart.addTag("kicadAttr", "smd")
newPart.addTag("kicad3DModel", "${KICAD6_3DMODEL_DIR}/LED_SMD.3dshapes/LED_SK6805_PLCC4_2.4x2.7mm_P1.3mm.wrl")

OOMP.parts.append(newPart)