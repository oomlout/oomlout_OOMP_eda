###### OOMP FILE  ######

import OOMP

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "kicad")
newPart.addTag("oompColor", "kicad-footprints")
newPart.addTag("oompDesc", "Capacitor_THT")
newPart.addTag("oompIndex", "C_Rect_L4.0mm_W2.5mm_P2.50mm")

newPart.addTag("kicadDesc", "C, Rect series, Radial, pin pitch=2.50mm, , length*width=4*2.5mm^2, Capacitor")
newPart.addTag("kicadTags", "C Rect series Radial pin pitch 2.50mm  length 4mm width 2.5mm Capacitor")
newPart.addTag("kicadAttr", "through_hole")
newPart.addTag("kicad3DModel", "${KICAD6_3DMODEL_DIR}/Capacitor_THT.3dshapes/C_Rect_L4.0mm_W2.5mm_P2.50mm.wrl")

OOMP.parts.append(newPart)