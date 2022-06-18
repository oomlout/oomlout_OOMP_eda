###### OOMP FILE  ######

import OOMP

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "kicad")
newPart.addTag("oompColor", "kicad-footprints")
newPart.addTag("oompDesc", "Capacitor_THT")
newPart.addTag("oompIndex", "CP_Radial_D35.0mm_P10.00mm_SnapIn")

newPart.addTag("kicadDesc", "CP, Radial series, Radial, pin pitch=10.00mm, , diameter=35mm, Electrolytic Capacitor, , http://www.vishay.com/docs/28342/058059pll-si.pdf")
newPart.addTag("kicadTags", "CP Radial series Radial pin pitch 10.00mm  diameter 35mm Electrolytic Capacitor")
newPart.addTag("kicadAttr", "through_hole")
newPart.addTag("kicad3DModel", "${KICAD6_3DMODEL_DIR}/Capacitor_THT.3dshapes/CP_Radial_D35.0mm_P10.00mm_SnapIn.wrl")

OOMP.parts.append(newPart)