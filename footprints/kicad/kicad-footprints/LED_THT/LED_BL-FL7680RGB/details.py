###### OOMP FILE  ######

import OOMP

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "kicad")
newPart.addTag("oompColor", "kicad-footprints")
newPart.addTag("oompDesc", "LED_THT")
newPart.addTag("oompIndex", "LED_BL-FL7680RGB")

newPart.addTag("kicadDesc", "'Piranha' RGB LED, through hole, common anode, 7.62x7.62mm, BGRA pin order, https://cdn-shop.adafruit.com/datasheets/BL-FL7680RGB.pdf")
newPart.addTag("kicadTags", "RGB LED Piranha Super-Flux BetLux")
newPart.addTag("kicadAttr", "through_hole")
newPart.addTag("kicad3DModel", "${KICAD6_3DMODEL_DIR}/LED_THT.3dshapes/LED_BL-FL7680RGB.wrl")

OOMP.parts.append(newPart)