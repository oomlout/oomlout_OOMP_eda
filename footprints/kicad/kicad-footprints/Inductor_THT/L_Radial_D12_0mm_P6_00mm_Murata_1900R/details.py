###### OOMP FILE  ######

import OOMP

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "kicad")
newPart.addTag("oompColor", "kicad-footprints")
newPart.addTag("oompDesc", "Inductor_THT")
newPart.addTag("oompIndex", "L_Radial_D12.0mm_P6.00mm_Murata_1900R")

newPart.addTag("kicadDesc", "Inductor, Radial series, Radial, pin pitch=6.00mm, , diameter=12.0mm, MuRATA, 1900R, http://www.murata-ps.com/data/magnetics/kmp_1900r.pdf")
newPart.addTag("kicadTags", "Inductor Radial series Radial pin pitch 6.00mm  diameter 12.0mm MuRATA 1900R")
newPart.addTag("kicadAttr", "through_hole")
newPart.addTag("kicad3DModel", "${KICAD6_3DMODEL_DIR}/Inductor_THT.3dshapes/L_Radial_D12.0mm_P6.00mm_Murata_1900R.wrl")

OOMP.parts.append(newPart)