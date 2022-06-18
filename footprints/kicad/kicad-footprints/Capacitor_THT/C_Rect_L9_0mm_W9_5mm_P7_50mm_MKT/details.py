###### OOMP FILE  ######

import OOMP

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "kicad")
newPart.addTag("oompColor", "kicad-footprints")
newPart.addTag("oompDesc", "Capacitor_THT")
newPart.addTag("oompIndex", "C_Rect_L9.0mm_W9.5mm_P7.50mm_MKT")

newPart.addTag("kicadDesc", "C, Rect series, Radial, pin pitch=7.50mm, , length*width=9*9.5mm^2, Capacitor, https://en.tdk.eu/inf/20/20/db/fc_2009/MKT_B32560_564.pdf")
newPart.addTag("kicadTags", "C Rect series Radial pin pitch 7.50mm  length 9mm width 9.5mm Capacitor")
newPart.addTag("kicadAttr", "through_hole")
newPart.addTag("kicad3DModel", "${KICAD6_3DMODEL_DIR}/Capacitor_THT.3dshapes/C_Rect_L9.0mm_W9.5mm_P7.50mm_MKT.wrl")

OOMP.parts.append(newPart)