###### OOMP FILE  ######

import OOMP

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "kicad")
newPart.addTag("oompColor", "kicad-footprints")
newPart.addTag("oompDesc", "LED_THT")
newPart.addTag("oompIndex", "LED_Rectangular_W3.9mm_H1.8mm")

newPart.addTag("kicadDesc", "LED_Rectangular, Rectangular,  Rectangular size 3.9x1.8mm^2, 2 pins, http://www.kingbright.com/attachments/file/psearch/000/00/00/L-2774GD(Ver.7B).pdf")
newPart.addTag("kicadTags", "LED_Rectangular Rectangular  Rectangular size 3.9x1.8mm^2 2 pins")
newPart.addTag("kicadAttr", "through_hole")
newPart.addTag("kicad3DModel", "${KICAD6_3DMODEL_DIR}/LED_THT.3dshapes/LED_Rectangular_W3.9mm_H1.8mm.wrl")

OOMP.parts.append(newPart)