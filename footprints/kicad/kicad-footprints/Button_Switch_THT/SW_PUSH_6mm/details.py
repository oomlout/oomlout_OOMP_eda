###### OOMP FILE  ######

import OOMP

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "kicad")
newPart.addTag("oompColor", "kicad-footprints")
newPart.addTag("oompDesc", "Button_Switch_THT")
newPart.addTag("oompIndex", "SW_PUSH_6mm")

newPart.addTag("kicadDesc", "https://www.omron.com/ecb/products/pdf/en-b3f.pdf")
newPart.addTag("kicadTags", "tact sw push 6mm")
newPart.addTag("kicadAttr", "through_hole")
newPart.addTag("kicad3DModel", "${KICAD6_3DMODEL_DIR}/Button_Switch_THT.3dshapes/SW_PUSH_6mm.wrl")

OOMP.parts.append(newPart)