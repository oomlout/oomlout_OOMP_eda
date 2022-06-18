###### OOMP FILE  ######

import OOMP

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "kicad")
newPart.addTag("oompColor", "kicad-footprints")
newPart.addTag("oompDesc", "Resistor_THT")
newPart.addTag("oompIndex", "R_Box_L13.0mm_W4.0mm_P9.00mm")

newPart.addTag("kicadDesc", "Resistor, Box series, Radial, pin pitch=9.00mm, 2W, length*width=13.0*4.0mm^2, http://www.produktinfo.conrad.com/datenblaetter/425000-449999/443860-da-01-de-METALLBAND_WIDERSTAND_0_1_OHM_5W_5Pr.pdf")
newPart.addTag("kicadTags", "Resistor Box series Radial pin pitch 9.00mm 2W length 13.0mm width 4.0mm")
newPart.addTag("kicadAttr", "through_hole")
newPart.addTag("kicad3DModel", "${KICAD6_3DMODEL_DIR}/Resistor_THT.3dshapes/R_Box_L13.0mm_W4.0mm_P9.00mm.wrl")

OOMP.parts.append(newPart)