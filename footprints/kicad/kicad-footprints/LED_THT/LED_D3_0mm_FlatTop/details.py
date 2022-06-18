###### OOMP FILE  ######

import OOMP

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "kicad")
newPart.addTag("oompColor", "kicad-footprints")
newPart.addTag("oompDesc", "LED_THT")
newPart.addTag("oompIndex", "LED_D3.0mm_FlatTop")

newPart.addTag("kicadDesc", "LED, Round, FlatTop, diameter 3.0mm, 2 pins, http://www.kingbright.com/attachments/file/psearch/000/00/00/L-47XEC(Ver.9A).pdf")
newPart.addTag("kicadTags", "LED Round FlatTop diameter 3.0mm 2 pins")
newPart.addTag("kicadAttr", "through_hole")
newPart.addTag("kicad3DModel", "${KICAD6_3DMODEL_DIR}/LED_THT.3dshapes/LED_D3.0mm_FlatTop.wrl")

OOMP.parts.append(newPart)