###### OOMP FILE  ######

import OOMP

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "kicad")
newPart.addTag("oompColor", "kicad-footprints")
newPart.addTag("oompDesc", "Resistor_THT")
newPart.addTag("oompIndex", "R_Box_L26.0mm_W5.0mm_P20.00mm")

newPart.addTag("kicadDesc", "Resistor, Box series, Radial, pin pitch=20.00mm, 10W, length*width=26.0*5.0mm^2, http://www.produktinfo.conrad.com/datenblaetter/425000-449999/443860-da-01-de-METALLBAND_WIDERSTAND_0_1_OHM_5W_5Pr.pdf")
newPart.addTag("kicadTags", "Resistor Box series Radial pin pitch 20.00mm 10W length 26.0mm width 5.0mm")
newPart.addTag("kicadAttr", "through_hole")
newPart.addTag("kicad3DModel", "${KICAD6_3DMODEL_DIR}/Resistor_THT.3dshapes/R_Box_L26.0mm_W5.0mm_P20.00mm.wrl")

OOMP.parts.append(newPart)