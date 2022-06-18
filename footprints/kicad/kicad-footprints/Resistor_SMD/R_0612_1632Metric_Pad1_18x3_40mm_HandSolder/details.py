###### OOMP FILE  ######

import OOMP

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "kicad")
newPart.addTag("oompColor", "kicad-footprints")
newPart.addTag("oompDesc", "Resistor_SMD")
newPart.addTag("oompIndex", "R_0612_1632Metric_Pad1.18x3.40mm_HandSolder")

newPart.addTag("kicadDesc", "Resistor SMD 0612 (1632 Metric), square (rectangular) end terminal, IPC_7351 nominal with elongated pad for handsoldering. (Body size source: https://www.vishay.com/docs/20019/rcwe.pdf), generated with kicad-footprint-generator")
newPart.addTag("kicadTags", "resistor handsolder")
newPart.addTag("kicadAttr", "smd")
newPart.addTag("kicad3DModel", "${KICAD6_3DMODEL_DIR}/Resistor_SMD.3dshapes/R_0612_1632Metric.wrl")

OOMP.parts.append(newPart)