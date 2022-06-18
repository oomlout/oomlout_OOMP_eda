###### OOMP FILE  ######

import OOMP

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "kicad")
newPart.addTag("oompColor", "kicad-footprints")
newPart.addTag("oompDesc", "LED_SMD")
newPart.addTag("oompIndex", "LED_Cree-PLCC4_5x5mm_CW")

newPart.addTag("kicadDesc", "5.0mm x 5.0mm PLCC4 LED")
newPart.addTag("kicadTags", "LED Cree PLCC-4")
newPart.addTag("kicadAttr", "smd")
newPart.addTag("kicad3DModel", "${KICAD6_3DMODEL_DIR}/LED_SMD.3dshapes/LED_Cree-PLCC4_5x5mm_CW.wrl")

OOMP.parts.append(newPart)