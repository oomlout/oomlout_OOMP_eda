###### OOMP FILE  ######

import OOMP

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "kicad")
newPart.addTag("oompColor", "kicad-footprints")
newPart.addTag("oompDesc", "LED_THT")
newPart.addTag("oompIndex", "LED_Oval_W5.2mm_H3.8mm")

newPart.addTag("kicadDesc", "LED_Oval, Oval,  Oval size 5.2x3.8mm^2, 2 pins, http://www.kingbright.com/attachments/file/psearch/000/00/00/L-5603QBC-D(Ver.12B).pdf")
newPart.addTag("kicadTags", "LED_Oval Oval  Oval size 5.2x3.8mm^2 2 pins")
newPart.addTag("kicadAttr", "through_hole")
newPart.addTag("kicad3DModel", "${KICAD6_3DMODEL_DIR}/LED_THT.3dshapes/LED_Oval_W5.2mm_H3.8mm.wrl")

OOMP.parts.append(newPart)