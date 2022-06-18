###### OOMP FILE  ######

import OOMP

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "kicad")
newPart.addTag("oompColor", "kicad-footprints")
newPart.addTag("oompDesc", "LED_THT")
newPart.addTag("oompIndex", "LED_D5.0mm-4_RGB_Wide_Pins")

newPart.addTag("kicadDesc", "LED, diameter 5.0mm, 4 pins, WP154A4, https://www.kingbright.com/attachments/file/psearch/000/00/00/L-154A4SUREQBFZGEW(Ver.11A).pdf")
newPart.addTag("kicadTags", "LED diameter 5.0mm 2 pins diameter 5.0mm 3 pins diameter 5.0mm 4 pins RGB RGBLED")
newPart.addTag("kicadAttr", "through_hole")
newPart.addTag("kicad3DModel", "${KICAD6_3DMODEL_DIR}/LED_THT.3dshapes/LED_D5.0mm-4_RGB_Wide_Pins.wrl")

OOMP.parts.append(newPart)