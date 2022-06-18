###### OOMP FILE  ######

import OOMP

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "kicad")
newPart.addTag("oompColor", "kicad-footprints")
newPart.addTag("oompDesc", "Resistor_THT")
newPart.addTag("oompIndex", "R_Bare_Metal_Element_L12.4mm_W4.8mm_P11.40mm")

newPart.addTag("kicadDesc", "Resistor, Bare_Metal_Element series, Bare Metal Strip/Wire, Horizontal, pin pitch=11.4mm, 1W, length*width=12.4*4.8mm^2, https://www.bourns.com/pdfs/PWR4412-2S.pdf")
newPart.addTag("kicadTags", "Resistor Bare_Metal_Element series Bare Metal Strip Wire Horizontal pin pitch 11.4mm 1W length 12.4mm width 4.8mm")
newPart.addTag("kicadAttr", "through_hole")
newPart.addTag("kicad3DModel", "${KICAD6_3DMODEL_DIR}/Resistor_THT.3dshapes/R_Bare_Metal_Element_L12.4mm_W4.8mm_P11.40mm.wrl")

OOMP.parts.append(newPart)