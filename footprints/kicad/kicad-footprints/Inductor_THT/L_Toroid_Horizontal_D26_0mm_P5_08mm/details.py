###### OOMP FILE  ######

import OOMP

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "kicad")
newPart.addTag("oompColor", "kicad-footprints")
newPart.addTag("oompDesc", "Inductor_THT")
newPart.addTag("oompIndex", "L_Toroid_Horizontal_D26.0mm_P5.08mm")

newPart.addTag("kicadDesc", "inductor 26mm diameter toroid")
newPart.addTag("kicadTags", "SELF INDUCTOR")
newPart.addTag("kicadAttr", "through_hole")
newPart.addTag("kicad3DModel", "${KICAD6_3DMODEL_DIR}/Inductor_THT.3dshapes/L_Toroid_Horizontal_D26.0mm_P5.08mm.wrl")

OOMP.parts.append(newPart)