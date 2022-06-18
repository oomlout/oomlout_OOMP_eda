###### OOMP FILE  ######

import OOMP

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "kicad")
newPart.addTag("oompColor", "kicad-footprints")
newPart.addTag("oompDesc", "Inductor_THT")
newPart.addTag("oompIndex", "L_Toroid_Vertical_L16.0mm_W8.0mm_P7.62mm")

newPart.addTag("kicadDesc", "L_Toroid, Vertical series, Radial, pin pitch=7.62mm, , length*width=16*8mm^2")
newPart.addTag("kicadTags", "L_Toroid Vertical series Radial pin pitch 7.62mm  length 16mm width 8mm")
newPart.addTag("kicadAttr", "through_hole")
newPart.addTag("kicad3DModel", "${KICAD6_3DMODEL_DIR}/Inductor_THT.3dshapes/L_Toroid_Vertical_L16.0mm_W8.0mm_P7.62mm.wrl")

OOMP.parts.append(newPart)