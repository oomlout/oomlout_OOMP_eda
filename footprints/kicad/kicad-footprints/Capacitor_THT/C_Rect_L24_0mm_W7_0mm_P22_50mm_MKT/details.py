###### OOMP FILE  ######

import OOMP

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "kicad")
newPart.addTag("oompColor", "kicad-footprints")
newPart.addTag("oompDesc", "Capacitor_THT")
newPart.addTag("oompIndex", "C_Rect_L24.0mm_W7.0mm_P22.50mm_MKT")

newPart.addTag("kicadDesc", "C, Rect series, Radial, pin pitch=22.50mm, , length*width=24*7mm^2, Capacitor, https://en.tdk.eu/inf/20/20/db/fc_2009/MKT_B32560_564.pdf")
newPart.addTag("kicadTags", "C Rect series Radial pin pitch 22.50mm  length 24mm width 7mm Capacitor")
newPart.addTag("kicadAttr", "through_hole")
newPart.addTag("kicad3DModel", "${KICAD6_3DMODEL_DIR}/Capacitor_THT.3dshapes/C_Rect_L24.0mm_W7.0mm_P22.50mm_MKT.wrl")

OOMP.parts.append(newPart)