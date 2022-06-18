###### OOMP FILE  ######

import OOMP

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "kicad")
newPart.addTag("oompColor", "kicad-footprints")
newPart.addTag("oompDesc", "Capacitor_THT")
newPart.addTag("oompIndex", "C_Disc_D3.8mm_W2.6mm_P2.50mm")

newPart.addTag("kicadDesc", "C, Disc series, Radial, pin pitch=2.50mm, , diameter*width=3.8*2.6mm^2, Capacitor, http://www.vishay.com/docs/45233/krseries.pdf")
newPart.addTag("kicadTags", "C Disc series Radial pin pitch 2.50mm  diameter 3.8mm width 2.6mm Capacitor")
newPart.addTag("kicadAttr", "through_hole")
newPart.addTag("kicad3DModel", "${KICAD6_3DMODEL_DIR}/Capacitor_THT.3dshapes/C_Disc_D3.8mm_W2.6mm_P2.50mm.wrl")

OOMP.parts.append(newPart)