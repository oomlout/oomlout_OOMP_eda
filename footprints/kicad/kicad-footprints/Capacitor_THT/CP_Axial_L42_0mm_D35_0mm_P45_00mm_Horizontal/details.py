###### OOMP FILE  ######

import OOMP

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "kicad")
newPart.addTag("oompColor", "kicad-footprints")
newPart.addTag("oompDesc", "Capacitor_THT")
newPart.addTag("oompIndex", "CP_Axial_L42.0mm_D35.0mm_P45.00mm_Horizontal")

newPart.addTag("kicadDesc", "CP, Axial series, Axial, Horizontal, pin pitch=45mm, , length*diameter=42*35.0mm^2, Electrolytic Capacitor, , http://www.vishay.com/docs/42037/53d.pdf")
newPart.addTag("kicadTags", "CP Axial series Axial Horizontal pin pitch 45mm  length 42mm diameter 35.0mm Electrolytic Capacitor")
newPart.addTag("kicadAttr", "through_hole")
newPart.addTag("kicad3DModel", "${KICAD6_3DMODEL_DIR}/Capacitor_THT.3dshapes/CP_Axial_L42.0mm_D35.0mm_P45.00mm_Horizontal.wrl")

OOMP.parts.append(newPart)