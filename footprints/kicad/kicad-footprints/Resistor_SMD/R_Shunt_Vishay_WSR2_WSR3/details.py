###### OOMP FILE  ######

import OOMP

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "kicad")
newPart.addTag("oompColor", "kicad-footprints")
newPart.addTag("oompDesc", "Resistor_SMD")
newPart.addTag("oompIndex", "R_Shunt_Vishay_WSR2_WSR3")

newPart.addTag("kicadDesc", "Power Metal Strip Resistors 0.005 to 0.2, https://www.vishay.com/docs/30101/wsr.pdf")
newPart.addTag("kicadTags", "SMD Shunt Resistor")
newPart.addTag("kicadAttr", "smd")
newPart.addTag("kicad3DModel", "${KICAD6_3DMODEL_DIR}/Resistor_SMD.3dshapes/R_Shunt_Vishay_WSR2_WSR3.wrl")

OOMP.parts.append(newPart)