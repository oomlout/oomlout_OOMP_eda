###### OOMP FILE  ######

import OOMP

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "kicad")
newPart.addTag("oompColor", "kicad-footprints")
newPart.addTag("oompDesc", "Capacitor_THT")
newPart.addTag("oompIndex", "C_Rect_L4.6mm_W2.0mm_P2.50mm_MKS02_FKP02")

newPart.addTag("kicadDesc", "C, Rect series, Radial, pin pitch=2.50mm, , length*width=4.6*2mm^2, Capacitor, http://www.wima.de/DE/WIMA_MKS_02.pdf")
newPart.addTag("kicadTags", "C Rect series Radial pin pitch 2.50mm  length 4.6mm width 2mm Capacitor")
newPart.addTag("kicadAttr", "through_hole")
newPart.addTag("kicad3DModel", "${KICAD6_3DMODEL_DIR}/Capacitor_THT.3dshapes/C_Rect_L4.6mm_W2.0mm_P2.50mm_MKS02_FKP02.wrl")

OOMP.parts.append(newPart)