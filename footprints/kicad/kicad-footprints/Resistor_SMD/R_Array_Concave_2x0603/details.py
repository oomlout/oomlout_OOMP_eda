###### OOMP FILE  ######

import OOMP

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "kicad")
newPart.addTag("oompColor", "kicad-footprints")
newPart.addTag("oompDesc", "Resistor_SMD")
newPart.addTag("oompIndex", "R_Array_Concave_2x0603")

newPart.addTag("kicadDesc", "Thick Film Chip Resistor Array, Wave soldering, Vishay CRA06P (see cra06p.pdf)")
newPart.addTag("kicadTags", "resistor array")
newPart.addTag("kicadAttr", "smd")
newPart.addTag("kicad3DModel", "${KICAD6_3DMODEL_DIR}/Resistor_SMD.3dshapes/R_Array_Concave_2x0603.wrl")

OOMP.parts.append(newPart)