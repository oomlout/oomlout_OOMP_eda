###### OOMP FILE  ######

import OOMP

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "kicad")
newPart.addTag("oompColor", "kicad-footprints")
newPart.addTag("oompDesc", "LED_THT")
newPart.addTag("oompIndex", "LED_D3.0mm_Clear")

newPart.addTag("kicadDesc", "IR-LED, diameter 3.0mm, 2 pins, color: clear")
newPart.addTag("kicadTags", "IR infrared LED diameter 3.0mm 2 pins clear")
newPart.addTag("kicadAttr", "through_hole")
newPart.addTag("kicad3DModel", "${KICAD6_3DMODEL_DIR}/LED_THT.3dshapes/LED_D3.0mm_Clear.wrl")

OOMP.parts.append(newPart)