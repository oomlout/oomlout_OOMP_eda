###### OOMP FILE  ######

import OOMP

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "kicad")
newPart.addTag("oompColor", "kicad-footprints")
newPart.addTag("oompDesc", "LED_SMD")
newPart.addTag("oompIndex", "LED_SK6812_EC15_1.5x1.5mm")

newPart.addTag("kicadDesc", "http://www.newstar-ledstrip.com/product/20181119172602110.pdf")
newPart.addTag("kicadTags", "LED RGB NeoPixel")
newPart.addTag("kicadAttr", "smd")
newPart.addTag("kicad3DModel", "${KICAD6_3DMODEL_DIR}/LED_SMD.3dshapes/LED_SK6812_EC15_1.5x1.5mm.wrl")

OOMP.parts.append(newPart)