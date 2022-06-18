###### OOMP FILE  ######

import OOMP

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "kicad")
newPart.addTag("oompColor", "kicad-footprints")
newPart.addTag("oompDesc", "Resistor_THT")
newPart.addTag("oompIndex", "R_Axial_Power_L50.0mm_W9.0mm_P60.96mm")

newPart.addTag("kicadDesc", "Resistor, Axial_Power series, Box, pin pitch=60.96mm, 11W, length*width*height=50*9*9mm^3, http://cdn-reichelt.de/documents/datenblatt/B400/5WAXIAL_9WAXIAL_11WAXIAL_17WAXIAL%23YAG.pdf")
newPart.addTag("kicadTags", "Resistor Axial_Power series Box pin pitch 60.96mm 11W length 50mm width 9mm height 9mm")
newPart.addTag("kicadAttr", "through_hole")
newPart.addTag("kicad3DModel", "${KICAD6_3DMODEL_DIR}/Resistor_THT.3dshapes/R_Axial_Power_L50.0mm_W9.0mm_P60.96mm.wrl")

OOMP.parts.append(newPart)