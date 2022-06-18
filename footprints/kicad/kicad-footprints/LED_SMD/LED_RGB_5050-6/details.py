###### OOMP FILE  ######

import OOMP

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "kicad")
newPart.addTag("oompColor", "kicad-footprints")
newPart.addTag("oompDesc", "LED_SMD")
newPart.addTag("oompIndex", "LED_RGB_5050-6")

newPart.addTag("kicadDesc", "http://cdn.sparkfun.com/datasheets/Components/LED/5060BRG4.pdf")
newPart.addTag("kicadTags", "RGB LED 5050-6")
newPart.addTag("kicadAttr", "smd")
newPart.addTag("kicad3DModel", "${KICAD6_3DMODEL_DIR}/LED_SMD.3dshapes/LED_RGB_5050-6.wrl")

OOMP.parts.append(newPart)