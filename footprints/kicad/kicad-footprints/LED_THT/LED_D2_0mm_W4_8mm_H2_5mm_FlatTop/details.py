###### OOMP FILE  ######

import OOMP

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "kicad")
newPart.addTag("oompColor", "kicad-footprints")
newPart.addTag("oompDesc", "LED_THT")
newPart.addTag("oompIndex", "LED_D2.0mm_W4.8mm_H2.5mm_FlatTop")

newPart.addTag("kicadDesc", "LED, Round, FlatTop,  Rectangular size 4.8x2.5mm^2 diameter 2.0mm, 2 pins, http://www.kingbright.com/attachments/file/psearch/000/00/00/L-13GD(Ver.11B).pdf")
newPart.addTag("kicadTags", "LED Round FlatTop  Rectangular size 4.8x2.5mm^2 diameter 2.0mm 2 pins")
newPart.addTag("kicadAttr", "through_hole")
newPart.addTag("kicad3DModel", "${KICAD6_3DMODEL_DIR}/LED_THT.3dshapes/LED_D2.0mm_W4.8mm_H2.5mm_FlatTop.wrl")

OOMP.parts.append(newPart)