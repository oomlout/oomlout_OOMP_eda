###### OOMP FILE  ######

import OOMP

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "kicad")
newPart.addTag("oompColor", "kicad-footprints")
newPart.addTag("oompDesc", "Diode_THT")
newPart.addTag("oompIndex", "D_T-1_P2.54mm_Vertical_AnodeUp")

newPart.addTag("kicadDesc", "Diode, T-1 series, Axial, Vertical, pin pitch=2.54mm, , length*diameter=3.2*2.6mm^2, , http://www.diodes.com/_files/packages/T-1.pdf")
newPart.addTag("kicadTags", "Diode T-1 series Axial Vertical pin pitch 2.54mm  length 3.2mm diameter 2.6mm")
newPart.addTag("kicadAttr", "through_hole")
newPart.addTag("kicad3DModel", "${KICAD6_3DMODEL_DIR}/Diode_THT.3dshapes/D_T-1_P2.54mm_Vertical_AnodeUp.wrl")

OOMP.parts.append(newPart)