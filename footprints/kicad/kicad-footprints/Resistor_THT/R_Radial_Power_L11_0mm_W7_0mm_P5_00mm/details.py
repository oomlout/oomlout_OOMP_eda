###### OOMP FILE  ######

import OOMP

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "kicad")
newPart.addTag("oompColor", "kicad-footprints")
newPart.addTag("oompDesc", "Resistor_THT")
newPart.addTag("oompIndex", "R_Radial_Power_L11.0mm_W7.0mm_P5.00mm")

newPart.addTag("kicadDesc", "Resistor, Radial_Power series, Radial, pin pitch=5.00mm, 2W, length*width=11.0*7.0mm^2, http://www.vishay.com/docs/30218/cpcx.pdf")
newPart.addTag("kicadTags", "Resistor Radial_Power series Radial pin pitch 5.00mm 2W length 11.0mm width 7.0mm")
newPart.addTag("kicadAttr", "through_hole")
newPart.addTag("kicad3DModel", "${KICAD6_3DMODEL_DIR}/Resistor_THT.3dshapes/R_Radial_Power_L11.0mm_W7.0mm_P5.00mm.wrl")

OOMP.parts.append(newPart)