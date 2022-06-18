###### OOMP FILE  ######

import OOMP

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "kicad")
newPart.addTag("oompColor", "kicad-footprints")
newPart.addTag("oompDesc", "Capacitor_THT")
newPart.addTag("oompIndex", "CP_Axial_L11.0mm_D8.0mm_P15.00mm_Horizontal")

newPart.addTag("kicadDesc", "CP, Axial series, Axial, Horizontal, pin pitch=15mm, , length*diameter=11*8mm^2, Electrolytic Capacitor, , http://www.vishay.com/docs/28325/021asm.pdf")
newPart.addTag("kicadTags", "CP Axial series Axial Horizontal pin pitch 15mm  length 11mm diameter 8mm Electrolytic Capacitor")
newPart.addTag("kicadAttr", "through_hole")
newPart.addTag("kicad3DModel", "${KICAD6_3DMODEL_DIR}/Capacitor_THT.3dshapes/CP_Axial_L11.0mm_D8.0mm_P15.00mm_Horizontal.wrl")

OOMP.parts.append(newPart)