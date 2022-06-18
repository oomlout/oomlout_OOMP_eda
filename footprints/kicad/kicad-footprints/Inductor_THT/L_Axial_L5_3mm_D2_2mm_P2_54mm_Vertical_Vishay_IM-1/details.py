###### OOMP FILE  ######

import OOMP

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "kicad")
newPart.addTag("oompColor", "kicad-footprints")
newPart.addTag("oompDesc", "Inductor_THT")
newPart.addTag("oompIndex", "L_Axial_L5.3mm_D2.2mm_P2.54mm_Vertical_Vishay_IM-1")

newPart.addTag("kicadDesc", "Inductor, Axial series, Axial, Vertical, pin pitch=2.54mm, , length*diameter=5.3*2.2mm^2, Vishay, IM-1, http://www.vishay.com/docs/34030/im.pdf")
newPart.addTag("kicadTags", "Inductor Axial series Axial Vertical pin pitch 2.54mm  length 5.3mm diameter 2.2mm Vishay IM-1")
newPart.addTag("kicadAttr", "through_hole")
newPart.addTag("kicad3DModel", "${KICAD6_3DMODEL_DIR}/Inductor_THT.3dshapes/L_Axial_L5.3mm_D2.2mm_P2.54mm_Vertical_Vishay_IM-1.wrl")

OOMP.parts.append(newPart)