###### OOMP FILE  ######

import OOMP

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "kicad")
newPart.addTag("oompColor", "kicad-footprints")
newPart.addTag("oompDesc", "Capacitor_THT")
newPart.addTag("oompIndex", "C_Axial_L22.0mm_D9.5mm_P27.50mm_Horizontal")

newPart.addTag("kicadDesc", "C, Axial series, Axial, Horizontal, pin pitch=27.5mm, , length*diameter=22*9.5mm^2, http://cdn-reichelt.de/documents/datenblatt/B300/STYROFLEX.pdf")
newPart.addTag("kicadTags", "C Axial series Axial Horizontal pin pitch 27.5mm  length 22mm diameter 9.5mm")
newPart.addTag("kicadAttr", "through_hole")
newPart.addTag("kicad3DModel", "${KICAD6_3DMODEL_DIR}/Capacitor_THT.3dshapes/C_Axial_L22.0mm_D9.5mm_P27.50mm_Horizontal.wrl")

OOMP.parts.append(newPart)