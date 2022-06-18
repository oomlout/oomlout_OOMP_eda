###### OOMP FILE  ######

import OOMP

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "kicad")
newPart.addTag("oompColor", "kicad-footprints")
newPart.addTag("oompDesc", "LED_THT")
newPart.addTag("oompIndex", "LED_D3.0mm-3")

newPart.addTag("kicadDesc", "LED, diameter 3.0mm, 2 pins, diameter 3.0mm, 3 pins, http://www.kingbright.com/attachments/file/psearch/000/00/00/L-3VSURKCGKC(Ver.8A).pdf")
newPart.addTag("kicadTags", "LED diameter 3.0mm 2 pins diameter 3.0mm 3 pins")
newPart.addTag("kicadAttr", "through_hole")
newPart.addTag("kicad3DModel", "${KICAD6_3DMODEL_DIR}/LED_THT.3dshapes/LED_D3.0mm-3.wrl")

OOMP.parts.append(newPart)