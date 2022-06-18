###### OOMP FILE  ######

import OOMP

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "kicad")
newPart.addTag("oompColor", "kicad-footprints")
newPart.addTag("oompDesc", "LED_SMD")
newPart.addTag("oompIndex", "LED_Inolux_IN-PI554FCH_PLCC4_5.0x5.0mm_P3.2mm")

newPart.addTag("kicadDesc", "http://www.inolux-corp.com/datasheet/SMDLED/Addressable%20LED/IN-PI554FCH.pdf")
newPart.addTag("kicadTags", "RGB LED NeoPixel addressable")
newPart.addTag("kicadAttr", "smd")
newPart.addTag("kicad3DModel", "${KICAD6_3DMODEL_DIR}/LED_SMD.3dshapes/LED_Inolux_IN-PI554FCH_PLCC4_5.0x5.0mm_P3.2mm.wrl")

OOMP.parts.append(newPart)