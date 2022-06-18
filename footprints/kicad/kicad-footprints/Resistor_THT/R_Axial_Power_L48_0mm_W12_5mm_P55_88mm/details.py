###### OOMP FILE  ######

import OOMP

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "kicad")
newPart.addTag("oompColor", "kicad-footprints")
newPart.addTag("oompDesc", "Resistor_THT")
newPart.addTag("oompIndex", "R_Axial_Power_L48.0mm_W12.5mm_P55.88mm")

newPart.addTag("kicadDesc", "Resistor, Axial_Power series, Box, pin pitch=55.88mm, 15W, length*width*height=48*12.5*12.5mm^3, http://cdn-reichelt.de/documents/datenblatt/B400/5WAXIAL_9WAXIAL_11WAXIAL_17WAXIAL%23YAG.pdf")
newPart.addTag("kicadTags", "Resistor Axial_Power series Box pin pitch 55.88mm 15W length 48mm width 12.5mm height 12.5mm")
newPart.addTag("kicadAttr", "through_hole")
newPart.addTag("kicad3DModel", "${KICAD6_3DMODEL_DIR}/Resistor_THT.3dshapes/R_Axial_Power_L48.0mm_W12.5mm_P55.88mm.wrl")

OOMP.parts.append(newPart)