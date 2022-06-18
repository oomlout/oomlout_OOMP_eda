###### OOMP FILE  ######

import OOMP

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "kicad")
newPart.addTag("oompColor", "kicad-footprints")
newPart.addTag("oompDesc", "Resistor_SMD")
newPart.addTag("oompIndex", "R_Array_Convex_2x0606")

newPart.addTag("kicadDesc", "Precision Thin Film Chip Resistor Array, VISHAY (see http://www.vishay.com/docs/28770/acasat.pdf)")
newPart.addTag("kicadTags", "resistor array")
newPart.addTag("kicadAttr", "smd")
newPart.addTag("kicad3DModel", "${KICAD6_3DMODEL_DIR}/Resistor_SMD.3dshapes/R_Array_Convex_2x0606.wrl")

OOMP.parts.append(newPart)