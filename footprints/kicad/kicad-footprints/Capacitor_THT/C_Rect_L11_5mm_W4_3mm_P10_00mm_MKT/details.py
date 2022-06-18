###### OOMP FILE  ######

import OOMP

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "kicad")
newPart.addTag("oompColor", "kicad-footprints")
newPart.addTag("oompDesc", "Capacitor_THT")
newPart.addTag("oompIndex", "C_Rect_L11.5mm_W4.3mm_P10.00mm_MKT")

newPart.addTag("kicadDesc", "C, Rect series, Radial, pin pitch=10.00mm, , length*width=11.5*4.3mm^2, Capacitor, https://en.tdk.eu/inf/20/20/db/fc_2009/MKT_B32560_564.pdf")
newPart.addTag("kicadTags", "C Rect series Radial pin pitch 10.00mm  length 11.5mm width 4.3mm Capacitor")
newPart.addTag("kicadAttr", "through_hole")
newPart.addTag("kicad3DModel", "${KICAD6_3DMODEL_DIR}/Capacitor_THT.3dshapes/C_Rect_L11.5mm_W4.3mm_P10.00mm_MKT.wrl")

OOMP.parts.append(newPart)