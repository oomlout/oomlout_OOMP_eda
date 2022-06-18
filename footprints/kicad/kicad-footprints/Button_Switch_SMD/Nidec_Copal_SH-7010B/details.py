###### OOMP FILE  ######

import OOMP

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "kicad")
newPart.addTag("oompColor", "kicad-footprints")
newPart.addTag("oompDesc", "Button_Switch_SMD")
newPart.addTag("oompIndex", "Nidec_Copal_SH-7010B")

newPart.addTag("kicadDesc", "4-bit rotary coded switch, gull wing, https://www.nidec-copal-electronics.com/e/catalog/switch/sh-7000.pdf")
newPart.addTag("kicadTags", "rotary switch bcd")
newPart.addTag("kicadAttr", "smd")
newPart.addTag("kicad3DModel", "${KICAD6_3DMODEL_DIR}/Button_Switch_SMD.3dshapes/Nidec_Copal_SH-7010B.wrl")

OOMP.parts.append(newPart)