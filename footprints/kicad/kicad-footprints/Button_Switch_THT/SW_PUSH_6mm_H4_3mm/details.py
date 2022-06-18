###### OOMP FILE  ######

import OOMP

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "kicad")
newPart.addTag("oompColor", "kicad-footprints")
newPart.addTag("oompDesc", "Button_Switch_THT")
newPart.addTag("oompIndex", "SW_PUSH_6mm_H4.3mm")

newPart.addTag("kicadDesc", "tactile push button, 6x6mm e.g. PHAP33xx series, height=4.3mm")
newPart.addTag("kicadTags", "tact sw push 6mm")
newPart.addTag("kicadAttr", "through_hole")
newPart.addTag("kicad3DModel", "${KICAD6_3DMODEL_DIR}/Button_Switch_THT.3dshapes/SW_PUSH_6mm_H4.3mm.wrl")

OOMP.parts.append(newPart)