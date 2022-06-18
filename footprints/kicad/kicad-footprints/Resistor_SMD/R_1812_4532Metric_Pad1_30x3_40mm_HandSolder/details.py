###### OOMP FILE  ######

import OOMP

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "kicad")
newPart.addTag("oompColor", "kicad-footprints")
newPart.addTag("oompDesc", "Resistor_SMD")
newPart.addTag("oompIndex", "R_1812_4532Metric_Pad1.30x3.40mm_HandSolder")

newPart.addTag("kicadDesc", "Resistor SMD 1812 (4532 Metric), square (rectangular) end terminal, IPC_7351 nominal with elongated pad for handsoldering. (Body size source: https://www.nikhef.nl/pub/departments/mt/projects/detectorR_D/dtddice/ERJ2G.pdf), generated with kicad-footprint-generator")
newPart.addTag("kicadTags", "resistor handsolder")
newPart.addTag("kicadAttr", "smd")
newPart.addTag("kicad3DModel", "${KICAD6_3DMODEL_DIR}/Resistor_SMD.3dshapes/R_1812_4532Metric.wrl")

OOMP.parts.append(newPart)