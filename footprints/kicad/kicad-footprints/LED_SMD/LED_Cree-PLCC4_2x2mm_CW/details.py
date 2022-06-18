###### OOMP FILE  ######

import OOMP

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "kicad")
newPart.addTag("oompColor", "kicad-footprints")
newPart.addTag("oompDesc", "LED_SMD")
newPart.addTag("oompIndex", "LED_Cree-PLCC4_2x2mm_CW")

newPart.addTag("kicadDesc", "2.0mm x 2.0mm PLCC4 LED, http://www.cree.com/~/media/Files/Cree/LED-Components-and-Modules/HB/Data-Sheets/CLMVBFKA.pdf")
newPart.addTag("kicadTags", "LED Cree PLCC-4")
newPart.addTag("kicadAttr", "smd")
newPart.addTag("kicad3DModel", "${KICAD6_3DMODEL_DIR}/LED_SMD.3dshapes/LED_Cree-PLCC4_2x2mm_CW.wrl")

OOMP.parts.append(newPart)