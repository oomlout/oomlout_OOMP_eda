###### OOMP FILE  ######

import OOMP

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "kicad")
newPart.addTag("oompColor", "kicad-footprints")
newPart.addTag("oompDesc", "Resistor_THT")
newPart.addTag("oompIndex", "R_Box_L8.4mm_W2.5mm_P5.08mm")

newPart.addTag("kicadDesc", "Resistor, Box series, Radial, pin pitch=5.08mm, 0.5W = 1/2W, length*width=8.38*2.54mm^2, http://www.vishay.com/docs/60051/cns020.pdf")
newPart.addTag("kicadTags", "Resistor Box series Radial pin pitch 5.08mm 0.5W = 1/2W length 8.38mm width 2.54mm")
newPart.addTag("kicadAttr", "through_hole")
newPart.addTag("kicad3DModel", "${KICAD6_3DMODEL_DIR}/Resistor_THT.3dshapes/R_Box_L8.4mm_W2.5mm_P5.08mm.wrl")

OOMP.parts.append(newPart)