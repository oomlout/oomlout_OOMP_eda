###### OOMP FILE  ######

import OOMP

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "kicad")
newPart.addTag("oompColor", "kicad-footprints")
newPart.addTag("oompDesc", "Resistor_THT")
newPart.addTag("oompIndex", "R_Radial_Power_L13.0mm_W9.0mm_P5.00mm")

newPart.addTag("kicadDesc", "Resistor, Radial_Power series, Radial, pin pitch=5.00mm, 7W, length*width=13.0*9.0mm^2, http://www.vishay.com/docs/30218/cpcx.pdf")
newPart.addTag("kicadTags", "Resistor Radial_Power series Radial pin pitch 5.00mm 7W length 13.0mm width 9.0mm")
newPart.addTag("kicadAttr", "through_hole")
newPart.addTag("kicad3DModel", "${KICAD6_3DMODEL_DIR}/Resistor_THT.3dshapes/R_Radial_Power_L13.0mm_W9.0mm_P5.00mm.wrl")

OOMP.parts.append(newPart)