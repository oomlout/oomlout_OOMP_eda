###### OOMP FILE  ######

import OOMP

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "kicad")
newPart.addTag("oompColor", "kicad-footprints")
newPart.addTag("oompDesc", "Inductor_THT")
newPart.addTag("oompIndex", "L_Radial_D10.5mm_P4.00x5.00mm_Murata_1200RS")

newPart.addTag("kicadDesc", "Inductor, Radial, Pitch=4.00x5.00mm, Diameter=10.5mm, Murata 1200RS, http://www.murata-ps.com/data/magnetics/kmp_1200rs.pdf")
newPart.addTag("kicadTags", "Inductor Radial Murata 1200RS")
newPart.addTag("kicadAttr", "through_hole")
newPart.addTag("kicad3DModel", "${KICAD6_3DMODEL_DIR}/Inductor_THT.3dshapes/L_Radial_D10.5mm_P4.00x5.00mm_Murata_1200RS.wrl")

OOMP.parts.append(newPart)