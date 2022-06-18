###### OOMP FILE  ######

import OOMP

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "kicad")
newPart.addTag("oompColor", "kicad-footprints")
newPart.addTag("oompDesc", "Inductor_THT")
newPart.addTag("oompIndex", "L_Radial_D7.2mm_P3.00mm_Murata_1700")

newPart.addTag("kicadDesc", "Inductor, Radial series, Radial, pin pitch=3.00mm, , diameter=7.2mm, MuRATA, 1700, http://www.murata-ps.com/data/magnetics/kmp_1700.pdf")
newPart.addTag("kicadTags", "Inductor Radial series Radial pin pitch 3.00mm  diameter 7.2mm MuRATA 1700")
newPart.addTag("kicadAttr", "through_hole")
newPart.addTag("kicad3DModel", "${KICAD6_3DMODEL_DIR}/Inductor_THT.3dshapes/L_Radial_D7.2mm_P3.00mm_Murata_1700.wrl")

OOMP.parts.append(newPart)