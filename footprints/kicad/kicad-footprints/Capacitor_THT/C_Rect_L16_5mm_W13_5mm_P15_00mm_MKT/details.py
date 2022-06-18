###### OOMP FILE  ######

import OOMP

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "kicad")
newPart.addTag("oompColor", "kicad-footprints")
newPart.addTag("oompDesc", "Capacitor_THT")
newPart.addTag("oompIndex", "C_Rect_L16.5mm_W13.5mm_P15.00mm_MKT")

newPart.addTag("kicadDesc", "C, Rect series, Radial, pin pitch=15.00mm, , length*width=16.5*13.5mm^2, Capacitor, https://en.tdk.eu/inf/20/20/db/fc_2009/MKT_B32560_564.pdf")
newPart.addTag("kicadTags", "C Rect series Radial pin pitch 15.00mm  length 16.5mm width 13.5mm Capacitor")
newPart.addTag("kicadAttr", "through_hole")
newPart.addTag("kicad3DModel", "${KICAD6_3DMODEL_DIR}/Capacitor_THT.3dshapes/C_Rect_L16.5mm_W13.5mm_P15.00mm_MKT.wrl")

OOMP.parts.append(newPart)