###### OOMP FILE  ######

import OOMP

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "kicad")
newPart.addTag("oompColor", "kicad-footprints")
newPart.addTag("oompDesc", "Capacitor_THT")
newPart.addTag("oompIndex", "C_Axial_L5.1mm_D3.1mm_P7.50mm_Horizontal")

newPart.addTag("kicadDesc", "C, Axial series, Axial, Horizontal, pin pitch=7.5mm, , length*diameter=5.1*3.1mm^2, http://www.vishay.com/docs/45231/arseries.pdf")
newPart.addTag("kicadTags", "C Axial series Axial Horizontal pin pitch 7.5mm  length 5.1mm diameter 3.1mm")
newPart.addTag("kicadAttr", "through_hole")
newPart.addTag("kicad3DModel", "${KICAD6_3DMODEL_DIR}/Capacitor_THT.3dshapes/C_Axial_L5.1mm_D3.1mm_P7.50mm_Horizontal.wrl")

OOMP.parts.append(newPart)