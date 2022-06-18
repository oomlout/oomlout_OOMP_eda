###### OOMP FILE  ######

import OOMP

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "kicad")
newPart.addTag("oompColor", "kicad-footprints")
newPart.addTag("oompDesc", "Capacitor_SMD")
newPart.addTag("oompIndex", "C_Elec_4x5.8")

newPart.addTag("kicadDesc", "SMD capacitor, aluminum electrolytic nonpolar, 4.0x5.8mm")
newPart.addTag("kicadTags", "capacitor electrolyic nonpolar")
newPart.addTag("kicadAttr", "smd")
newPart.addTag("kicad3DModel", "${KICAD6_3DMODEL_DIR}/Capacitor_SMD.3dshapes/C_Elec_4x5.8.wrl")

OOMP.parts.append(newPart)