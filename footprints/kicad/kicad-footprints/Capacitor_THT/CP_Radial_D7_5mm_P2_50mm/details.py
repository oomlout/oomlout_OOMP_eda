###### OOMP FILE  ######

import OOMP

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "kicad")
newPart.addTag("oompColor", "kicad-footprints")
newPart.addTag("oompDesc", "Capacitor_THT")
newPart.addTag("oompIndex", "CP_Radial_D7.5mm_P2.50mm")

newPart.addTag("kicadDesc", "CP, Radial series, Radial, pin pitch=2.50mm, , diameter=7.5mm, Electrolytic Capacitor")
newPart.addTag("kicadTags", "CP Radial series Radial pin pitch 2.50mm  diameter 7.5mm Electrolytic Capacitor")
newPart.addTag("kicadAttr", "through_hole")
newPart.addTag("kicad3DModel", "${KICAD6_3DMODEL_DIR}/Capacitor_THT.3dshapes/CP_Radial_D7.5mm_P2.50mm.wrl")

OOMP.parts.append(newPart)