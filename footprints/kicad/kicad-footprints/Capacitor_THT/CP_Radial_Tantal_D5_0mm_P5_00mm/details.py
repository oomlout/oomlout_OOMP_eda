###### OOMP FILE  ######

import OOMP

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "kicad")
newPart.addTag("oompColor", "kicad-footprints")
newPart.addTag("oompDesc", "Capacitor_THT")
newPart.addTag("oompIndex", "CP_Radial_Tantal_D5.0mm_P5.00mm")

newPart.addTag("kicadDesc", "CP, Radial_Tantal series, Radial, pin pitch=5.00mm, , diameter=5.0mm, Tantal Electrolytic Capacitor, http://cdn-reichelt.de/documents/datenblatt/B300/TANTAL-TB-Serie%23.pdf")
newPart.addTag("kicadTags", "CP Radial_Tantal series Radial pin pitch 5.00mm  diameter 5.0mm Tantal Electrolytic Capacitor")
newPart.addTag("kicadAttr", "through_hole")
newPart.addTag("kicad3DModel", "${KICAD6_3DMODEL_DIR}/Capacitor_THT.3dshapes/CP_Radial_Tantal_D5.0mm_P5.00mm.wrl")

OOMP.parts.append(newPart)