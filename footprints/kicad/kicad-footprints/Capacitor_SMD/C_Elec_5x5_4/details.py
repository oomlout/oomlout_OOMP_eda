###### OOMP FILE  ######

import OOMP

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "kicad")
newPart.addTag("oompColor", "kicad-footprints")
newPart.addTag("oompDesc", "Capacitor_SMD")
newPart.addTag("oompIndex", "C_Elec_5x5.4")

newPart.addTag("kicadDesc", "SMD capacitor, aluminum electrolytic nonpolar, 5.0x5.4mm")
newPart.addTag("kicadTags", "capacitor electrolyic nonpolar")
newPart.addTag("kicadAttr", "smd")
newPart.addTag("kicad3DModel", "${KICAD6_3DMODEL_DIR}/Capacitor_SMD.3dshapes/C_Elec_5x5.4.wrl")

OOMP.parts.append(newPart)