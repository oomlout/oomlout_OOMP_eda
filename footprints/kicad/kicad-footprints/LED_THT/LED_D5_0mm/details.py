###### OOMP FILE  ######

import OOMP

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "kicad")
newPart.addTag("oompColor", "kicad-footprints")
newPart.addTag("oompDesc", "LED_THT")
newPart.addTag("oompIndex", "LED_D5.0mm")

newPart.addTag("kicadDesc", "LED, diameter 5.0mm, 2 pins, http://cdn-reichelt.de/documents/datenblatt/A500/LL-504BC2E-009.pdf")
newPart.addTag("kicadTags", "LED diameter 5.0mm 2 pins")
newPart.addTag("kicadAttr", "through_hole")
newPart.addTag("kicad3DModel", "${KICAD6_3DMODEL_DIR}/LED_THT.3dshapes/LED_D5.0mm.wrl")

OOMP.parts.append(newPart)