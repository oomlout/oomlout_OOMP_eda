###### OOMP FILE  ######

import OOMP

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "kicad")
newPart.addTag("oompColor", "kicad-footprints")
newPart.addTag("oompDesc", "Capacitor_SMD")
newPart.addTag("oompIndex", "C_0201_0603Metric_Pad0.64x0.40mm_HandSolder")

newPart.addTag("kicadDesc", "Capacitor SMD 0201 (0603 Metric), square (rectangular) end terminal, IPC_7351 nominal with elongated pad for handsoldering. (Body size source: https://www.vishay.com/docs/20052/crcw0201e3.pdf), generated with kicad-footprint-generator")
newPart.addTag("kicadTags", "capacitor handsolder")
newPart.addTag("kicadAttr", "smd")
newPart.addTag("kicad3DModel", "${KICAD6_3DMODEL_DIR}/Capacitor_SMD.3dshapes/C_0201_0603Metric.wrl")

OOMP.parts.append(newPart)