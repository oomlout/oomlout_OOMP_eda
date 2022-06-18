###### OOMP FILE  ######

import OOMP

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "kicad")
newPart.addTag("oompColor", "kicad-footprints")
newPart.addTag("oompDesc", "LED_SMD")
newPart.addTag("oompIndex", "LED_Luminus_MP-3030-1100_3.0x3.0mm")

newPart.addTag("kicadDesc", "Mid Power LED, Luminus MP-3030-1100, 3.0x3.0mm, 816mW, https://download.luminus.com/datasheets/Luminus_MP3030_1100_Datasheet.pdf")
newPart.addTag("kicadTags", "LED Luminus MP-3030-1100")
newPart.addTag("kicadAttr", "smd")
newPart.addTag("kicad3DModel", "${KICAD6_3DMODEL_DIR}/LED_SMD.3dshapes/LED_Luminus_MP-3030-1100_3.0x3.0mm.wrl")

OOMP.parts.append(newPart)