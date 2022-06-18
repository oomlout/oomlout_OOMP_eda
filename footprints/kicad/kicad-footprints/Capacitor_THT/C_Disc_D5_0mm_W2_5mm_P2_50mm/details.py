###### OOMP FILE  ######

import OOMP

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "kicad")
newPart.addTag("oompColor", "kicad-footprints")
newPart.addTag("oompDesc", "Capacitor_THT")
newPart.addTag("oompIndex", "C_Disc_D5.0mm_W2.5mm_P2.50mm")

newPart.addTag("kicadDesc", "C, Disc series, Radial, pin pitch=2.50mm, , diameter*width=5*2.5mm^2, Capacitor, http://cdn-reichelt.de/documents/datenblatt/B300/DS_KERKO_TC.pdf")
newPart.addTag("kicadTags", "C Disc series Radial pin pitch 2.50mm  diameter 5mm width 2.5mm Capacitor")
newPart.addTag("kicadAttr", "through_hole")
newPart.addTag("kicad3DModel", "${KICAD6_3DMODEL_DIR}/Capacitor_THT.3dshapes/C_Disc_D5.0mm_W2.5mm_P2.50mm.wrl")

OOMP.parts.append(newPart)