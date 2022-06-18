###### OOMP FILE  ######

import OOMP

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "kicad")
newPart.addTag("oompColor", "kicad-footprints")
newPart.addTag("oompDesc", "Resistor_THT")
newPart.addTag("oompIndex", "R_Axial_Power_L25.0mm_W6.4mm_P30.48mm")

newPart.addTag("kicadDesc", "Resistor, Axial_Power series, Box, pin pitch=30.48mm, 5W, length*width*height=25*6.4*6.4mm^3, http://cdn-reichelt.de/documents/datenblatt/B400/5WAXIAL_9WAXIAL_11WAXIAL_17WAXIAL%23YAG.pdf")
newPart.addTag("kicadTags", "Resistor Axial_Power series Box pin pitch 30.48mm 5W length 25mm width 6.4mm height 6.4mm")
newPart.addTag("kicadAttr", "through_hole")
newPart.addTag("kicad3DModel", "${KICAD6_3DMODEL_DIR}/Resistor_THT.3dshapes/R_Axial_Power_L25.0mm_W6.4mm_P30.48mm.wrl")

OOMP.parts.append(newPart)