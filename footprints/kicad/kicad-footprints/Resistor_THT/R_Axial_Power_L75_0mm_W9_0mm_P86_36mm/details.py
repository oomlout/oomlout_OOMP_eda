###### OOMP FILE  ######

import OOMP

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "kicad")
newPart.addTag("oompColor", "kicad-footprints")
newPart.addTag("oompDesc", "Resistor_THT")
newPart.addTag("oompIndex", "R_Axial_Power_L75.0mm_W9.0mm_P86.36mm")

newPart.addTag("kicadDesc", "Resistor, Axial_Power series, Box, pin pitch=86.36mm, 17W, length*width*height=75*9*9mm^3, http://cdn-reichelt.de/documents/datenblatt/B400/5WAXIAL_9WAXIAL_11WAXIAL_17WAXIAL%23YAG.pdf")
newPart.addTag("kicadTags", "Resistor Axial_Power series Box pin pitch 86.36mm 17W length 75mm width 9mm height 9mm")
newPart.addTag("kicadAttr", "through_hole")
newPart.addTag("kicad3DModel", "${KICAD6_3DMODEL_DIR}/Resistor_THT.3dshapes/R_Axial_Power_L75.0mm_W9.0mm_P86.36mm.wrl")

OOMP.parts.append(newPart)