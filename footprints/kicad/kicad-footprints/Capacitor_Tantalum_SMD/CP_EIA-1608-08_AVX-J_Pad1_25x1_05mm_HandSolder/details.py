###### OOMP FILE  ######

import OOMP

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "kicad")
newPart.addTag("oompColor", "kicad-footprints")
newPart.addTag("oompDesc", "Capacitor_Tantalum_SMD")
newPart.addTag("oompIndex", "CP_EIA-1608-08_AVX-J_Pad1.25x1.05mm_HandSolder")

newPart.addTag("kicadDesc", "Tantalum Capacitor SMD AVX-J (1608-08 Metric), IPC_7351 nominal, (Body size from: https://www.vishay.com/docs/48064/_t58_vmn_pt0471_1601.pdf), generated with kicad-footprint-generator")
newPart.addTag("kicadTags", "capacitor tantalum")
newPart.addTag("kicadAttr", "smd")
newPart.addTag("kicad3DModel", "${KICAD6_3DMODEL_DIR}/Capacitor_Tantalum_SMD.3dshapes/CP_EIA-1608-08_AVX-J.wrl")

OOMP.parts.append(newPart)