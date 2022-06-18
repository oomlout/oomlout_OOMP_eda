###### OOMP FILE  ######

import OOMP

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "kicad")
newPart.addTag("oompColor", "kicad-footprints")
newPart.addTag("oompDesc", "Capacitor_THT")
newPart.addTag("oompIndex", "C_Disc_D7.5mm_W5.0mm_P10.00mm")

newPart.addTag("kicadDesc", "C, Disc series, Radial, pin pitch=10.00mm, , diameter*width=7.5*5.0mm^2, Capacitor, http://www.vishay.com/docs/28535/vy2series.pdf")
newPart.addTag("kicadTags", "C Disc series Radial pin pitch 10.00mm  diameter 7.5mm width 5.0mm Capacitor")
newPart.addTag("kicadAttr", "through_hole")
newPart.addTag("kicad3DModel", "${KICAD6_3DMODEL_DIR}/Capacitor_THT.3dshapes/C_Disc_D7.5mm_W5.0mm_P10.00mm.wrl")

OOMP.parts.append(newPart)