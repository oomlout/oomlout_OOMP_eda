###### OOMP FILE  ######

import OOMP

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "kicad")
newPart.addTag("oompColor", "kicad-footprints")
newPart.addTag("oompDesc", "Diode_THT")
newPart.addTag("oompIndex", "D_P600_R-6_P20.00mm_Horizontal")

newPart.addTag("kicadDesc", "Diode, P600_R-6 series, Axial, Horizontal, pin pitch=20mm, , length*diameter=9.1*9.1mm^2, , http://www.vishay.com/docs/88692/p600a.pdf, http://www.diodes.com/_files/packages/R-6.pdf")
newPart.addTag("kicadTags", "Diode P600_R-6 series Axial Horizontal pin pitch 20mm  length 9.1mm diameter 9.1mm")
newPart.addTag("kicadAttr", "through_hole")
newPart.addTag("kicad3DModel", "${KICAD6_3DMODEL_DIR}/Diode_THT.3dshapes/D_P600_R-6_P20.00mm_Horizontal.wrl")

OOMP.parts.append(newPart)