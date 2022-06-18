###### OOMP FILE  ######

import OOMP

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "kicad")
newPart.addTag("oompColor", "kicad-footprints")
newPart.addTag("oompDesc", "Resistor_THT")
newPart.addTag("oompIndex", "R_Axial_DIN0414_L11.9mm_D4.5mm_P25.40mm_Horizontal")

newPart.addTag("kicadDesc", "Resistor, Axial_DIN0414 series, Axial, Horizontal, pin pitch=25.4mm, 2W, length*diameter=11.9*4.5mm^2, http://www.vishay.com/docs/20128/wkxwrx.pdf")
newPart.addTag("kicadTags", "Resistor Axial_DIN0414 series Axial Horizontal pin pitch 25.4mm 2W length 11.9mm diameter 4.5mm")
newPart.addTag("kicadAttr", "through_hole")
newPart.addTag("kicad3DModel", "${KICAD6_3DMODEL_DIR}/Resistor_THT.3dshapes/R_Axial_DIN0414_L11.9mm_D4.5mm_P25.40mm_Horizontal.wrl")

OOMP.parts.append(newPart)