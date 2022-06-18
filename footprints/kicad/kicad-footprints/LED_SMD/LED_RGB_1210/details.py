###### OOMP FILE  ######

import OOMP

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "kicad")
newPart.addTag("oompColor", "kicad-footprints")
newPart.addTag("oompDesc", "LED_SMD")
newPart.addTag("oompIndex", "LED_RGB_1210")

newPart.addTag("kicadDesc", "RGB LED 3.2x2.7mm http://www.avagotech.com/docs/AV02-0610EN")
newPart.addTag("kicadTags", "LED 3227")
newPart.addTag("kicadAttr", "smd")
newPart.addTag("kicad3DModel", "${KICAD6_3DMODEL_DIR}/LED_SMD.3dshapes/LED_RGB_1210.wrl")

OOMP.parts.append(newPart)