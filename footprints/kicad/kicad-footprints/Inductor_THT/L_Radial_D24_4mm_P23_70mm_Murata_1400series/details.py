###### OOMP FILE  ######

import OOMP

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "kicad")
newPart.addTag("oompColor", "kicad-footprints")
newPart.addTag("oompDesc", "Inductor_THT")
newPart.addTag("oompIndex", "L_Radial_D24.4mm_P23.70mm_Murata_1400series")

newPart.addTag("kicadDesc", "Inductor, Radial series, Radial, pin pitch=23.70mm, , diameter=24.4mm, muRATA, 1400series, http://www.murata-ps.com/data/magnetics/kmp_1400.pdf")
newPart.addTag("kicadTags", "Inductor Radial series Radial pin pitch 23.70mm  diameter 24.4mm muRATA 1400series")
newPart.addTag("kicadAttr", "through_hole")
newPart.addTag("kicad3DModel", "${KICAD6_3DMODEL_DIR}/Inductor_THT.3dshapes/L_Radial_D24.4mm_P23.70mm_Murata_1400series.wrl")

OOMP.parts.append(newPart)