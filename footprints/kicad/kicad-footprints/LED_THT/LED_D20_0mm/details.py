###### OOMP FILE  ######

import OOMP

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "kicad")
newPart.addTag("oompColor", "kicad-footprints")
newPart.addTag("oompDesc", "LED_THT")
newPart.addTag("oompIndex", "LED_D20.0mm")
newPart.addTag("oompName", "kicad-footprints/LED_THT/LED_D20.0mm")

newPart.addTag("kicadDesc", "LED, diameter 20.0mm, 2 pins, http://cdn-reichelt.de/documents/datenblatt/A500/DLC2-6GD%28V6%29.pdf")
newPart.addTag("kicadTags", "LED diameter 20.0mm 2 pins")
newPart.addTag("kicadAttr", "through_hole")
newPart.addTag("kicad3DModel", "${KICAD6_3DMODEL_DIR}/LED_THT.3dshapes/LED_D20.0mm.wrl")

OOMP.parts.append(newPart)