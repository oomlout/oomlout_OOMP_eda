###### OOMP FILE  ######

import OOMP

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "kicad")
newPart.addTag("oompColor", "kicad-footprints")
newPart.addTag("oompDesc", "LED_SMD")
newPart.addTag("oompIndex", "LED_CSP_Samsung_LH181B_2.36x2.36mm")

newPart.addTag("kicadDesc", "High Power CSP LED, 2.36mm x 2.36mm, 1.4A max, https://cdn.samsung.com/led/file/resource/2021/01/Data_Sheet_LH181B_Rev.4.0.pdf")
newPart.addTag("kicadTags", "LED Samsung LH181B")
newPart.addTag("kicadAttr", "smd")
newPart.addTag("kicad3DModel", "${KICAD6_3DMODEL_DIR}/LED_SMD.3dshapes/LED_CSP_Samsung_LH181B_2.36x2.36mm.wrl")

OOMP.parts.append(newPart)