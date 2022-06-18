###### OOMP FILE  ######

import OOMP

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "kicad")
newPart.addTag("oompColor", "kicad-footprints")
newPart.addTag("oompDesc", "LED_SMD")
newPart.addTag("oompIndex", "LED_1812_4532Metric_Pad1.30x3.40mm_HandSolder")

newPart.addTag("kicadDesc", "LED SMD 1812 (4532 Metric), square (rectangular) end terminal, IPC_7351 nominal, (Body size source: https://www.nikhef.nl/pub/departments/mt/projects/detectorR_D/dtddice/ERJ2G.pdf), generated with kicad-footprint-generator")
newPart.addTag("kicadTags", "LED handsolder")
newPart.addTag("kicadAttr", "smd")
newPart.addTag("kicad3DModel", "${KICAD6_3DMODEL_DIR}/LED_SMD.3dshapes/LED_1812_4532Metric.wrl")

OOMP.parts.append(newPart)