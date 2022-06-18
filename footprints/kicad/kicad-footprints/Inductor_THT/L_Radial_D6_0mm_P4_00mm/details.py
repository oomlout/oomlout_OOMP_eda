###### OOMP FILE  ######

import OOMP

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "kicad")
newPart.addTag("oompColor", "kicad-footprints")
newPart.addTag("oompDesc", "Inductor_THT")
newPart.addTag("oompIndex", "L_Radial_D6.0mm_P4.00mm")

newPart.addTag("kicadDesc", "Inductor, Radial series, Radial, pin pitch=4.00mm, , diameter=6.0mm, http://www.abracon.com/Magnetics/radial/AIUR-07.pdf")
newPart.addTag("kicadTags", "Inductor Radial series Radial pin pitch 4.00mm  diameter 6.0mm")
newPart.addTag("kicadAttr", "through_hole")
newPart.addTag("kicad3DModel", "${KICAD6_3DMODEL_DIR}/Inductor_THT.3dshapes/L_Radial_D6.0mm_P4.00mm.wrl")

OOMP.parts.append(newPart)