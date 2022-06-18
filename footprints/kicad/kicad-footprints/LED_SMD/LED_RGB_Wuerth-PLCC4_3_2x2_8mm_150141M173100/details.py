###### OOMP FILE  ######

import OOMP

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "kicad")
newPart.addTag("oompColor", "kicad-footprints")
newPart.addTag("oompDesc", "LED_SMD")
newPart.addTag("oompIndex", "LED_RGB_Wuerth-PLCC4_3.2x2.8mm_150141M173100")

newPart.addTag("kicadDesc", "3.2mm x 2.8mm PLCC4 LED, https://www.we-online.de/katalog/datasheet/150141M173100.pdf")
newPart.addTag("kicadTags", "LED RGB Wurth PLCC-4")
newPart.addTag("kicadAttr", "smd")
newPart.addTag("kicad3DModel", "${KICAD6_3DMODEL_DIR}/LED_SMD.3dshapes/LED_RGB_Wuerth-PLCC4_3.2x2.8mm_150141M173100.wrl")

OOMP.parts.append(newPart)