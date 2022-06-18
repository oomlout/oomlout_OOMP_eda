###### OOMP FILE  ######

import OOMP

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "kicad")
newPart.addTag("oompColor", "kicad-footprints")
newPart.addTag("oompDesc", "Capacitor_THT")
newPart.addTag("oompIndex", "C_Axial_L12.0mm_D10.5mm_P20.00mm_Horizontal")

newPart.addTag("kicadDesc", "C, Axial series, Axial, Horizontal, pin pitch=20mm, , length*diameter=12*10.5mm^2, http://cdn-reichelt.de/documents/datenblatt/B300/STYROFLEX.pdf")
newPart.addTag("kicadTags", "C Axial series Axial Horizontal pin pitch 20mm  length 12mm diameter 10.5mm")
newPart.addTag("kicadAttr", "through_hole")
newPart.addTag("kicad3DModel", "${KICAD6_3DMODEL_DIR}/Capacitor_THT.3dshapes/C_Axial_L12.0mm_D10.5mm_P20.00mm_Horizontal.wrl")

OOMP.parts.append(newPart)