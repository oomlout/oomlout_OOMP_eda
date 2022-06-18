###### OOMP FILE  ######

import OOMP

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "kicad")
newPart.addTag("oompColor", "kicad-footprints")
newPart.addTag("oompDesc", "LED_SMD")
newPart.addTag("oompIndex", "LED_SK6812MINI_PLCC4_3.5x3.5mm_P1.75mm")

newPart.addTag("kicadDesc", "https://cdn-shop.adafruit.com/product-files/2686/SK6812MINI_REV.01-1-2.pdf")
newPart.addTag("kicadTags", "LED RGB NeoPixel Mini")
newPart.addTag("kicadAttr", "smd")
newPart.addTag("kicad3DModel", "${KICAD6_3DMODEL_DIR}/LED_SMD.3dshapes/LED_SK6812MINI_PLCC4_3.5x3.5mm_P1.75mm.wrl")

OOMP.parts.append(newPart)