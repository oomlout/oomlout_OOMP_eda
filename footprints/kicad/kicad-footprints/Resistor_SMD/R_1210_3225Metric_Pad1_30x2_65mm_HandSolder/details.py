###### OOMP FILE  ######

import OOMP

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "kicad")
newPart.addTag("oompColor", "kicad-footprints")
newPart.addTag("oompDesc", "Resistor_SMD")
newPart.addTag("oompIndex", "R_1210_3225Metric_Pad1.30x2.65mm_HandSolder")

newPart.addTag("kicadDesc", "Resistor SMD 1210 (3225 Metric), square (rectangular) end terminal, IPC_7351 nominal with elongated pad for handsoldering. (Body size source: IPC-SM-782 page 72, https://www.pcb-3d.com/wordpress/wp-content/uploads/ipc-sm-782a_amendment_1_and_2.pdf), generated with kicad-footprint-generator")
newPart.addTag("kicadTags", "resistor handsolder")
newPart.addTag("kicadAttr", "smd")
newPart.addTag("kicad3DModel", "${KICAD6_3DMODEL_DIR}/Resistor_SMD.3dshapes/R_1210_3225Metric.wrl")

OOMP.parts.append(newPart)