###### OOMP FILE  ######

import OOMP

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "kicad")
newPart.addTag("oompColor", "kicad-footprints")
newPart.addTag("oompDesc", "Capacitor_SMD")
newPart.addTag("oompIndex", "CP_Elec_16x22")

newPart.addTag("kicadDesc", "SMD capacitor, aluminum electrolytic, Vishay 1621, 16.0x22.0mm, http://www.vishay.com/docs/28395/150crz.pdf")
newPart.addTag("kicadTags", "capacitor electrolytic")
newPart.addTag("kicadAttr", "smd")
newPart.addTag("kicad3DModel", "${KICAD6_3DMODEL_DIR}/Capacitor_SMD.3dshapes/CP_Elec_16x22.wrl")

OOMP.parts.append(newPart)