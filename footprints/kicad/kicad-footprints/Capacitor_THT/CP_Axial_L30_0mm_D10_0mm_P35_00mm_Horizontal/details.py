###### OOMP FILE  ######

import OOMP

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "kicad")
newPart.addTag("oompColor", "kicad-footprints")
newPart.addTag("oompDesc", "Capacitor_THT")
newPart.addTag("oompIndex", "CP_Axial_L30.0mm_D10.0mm_P35.00mm_Horizontal")

newPart.addTag("kicadDesc", "CP, Axial series, Axial, Horizontal, pin pitch=35mm, , length*diameter=30*10mm^2, Electrolytic Capacitor, , http://www.vishay.com/docs/28325/021asm.pdf")
newPart.addTag("kicadTags", "CP Axial series Axial Horizontal pin pitch 35mm  length 30mm diameter 10mm Electrolytic Capacitor")
newPart.addTag("kicadAttr", "through_hole")
newPart.addTag("kicad3DModel", "${KICAD6_3DMODEL_DIR}/Capacitor_THT.3dshapes/CP_Axial_L30.0mm_D10.0mm_P35.00mm_Horizontal.wrl")

OOMP.parts.append(newPart)