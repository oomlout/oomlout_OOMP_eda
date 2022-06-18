###### OOMP FILE  ######

import OOMP

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "kicad")
newPart.addTag("oompColor", "kicad-footprints")
newPart.addTag("oompDesc", "Resistor_SMD")
newPart.addTag("oompIndex", "R_Array_Convex_2x1206")

newPart.addTag("kicadDesc", "Chip Resistor Network, ROHM MNR32 (see mnr_g.pdf)")
newPart.addTag("kicadTags", "resistor array")
newPart.addTag("kicadAttr", "smd")
newPart.addTag("kicad3DModel", "${KICAD6_3DMODEL_DIR}/Resistor_SMD.3dshapes/R_Array_Convex_2x1206.wrl")

OOMP.parts.append(newPart)