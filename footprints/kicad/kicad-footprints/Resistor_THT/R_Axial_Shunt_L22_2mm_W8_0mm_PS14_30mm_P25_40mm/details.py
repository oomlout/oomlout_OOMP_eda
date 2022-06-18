###### OOMP FILE  ######

import OOMP

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "kicad")
newPart.addTag("oompColor", "kicad-footprints")
newPart.addTag("oompDesc", "Resistor_THT")
newPart.addTag("oompIndex", "R_Axial_Shunt_L22.2mm_W8.0mm_PS14.30mm_P25.40mm")

newPart.addTag("kicadDesc", "Resistor, Axial_Shunt series, Box, pin pitch=25.4mm, 3W, length*width*height=22.2*8*8mm^3, shunt pin pitch = 14.30mm, http://www.vishay.com/docs/30217/cpsl.pdf")
newPart.addTag("kicadTags", "Resistor Axial_Shunt series Box pin pitch 25.4mm 3W length 22.2mm width 8mm height 8mm shunt pin pitch 14.30mm")
newPart.addTag("kicadAttr", "through_hole")
newPart.addTag("kicad3DModel", "${KICAD6_3DMODEL_DIR}/Resistor_THT.3dshapes/R_Axial_Shunt_L22.2mm_W8.0mm_PS14.30mm_P25.40mm.wrl")

OOMP.parts.append(newPart)