###### OOMP FILE  ######

import OOMP

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "kicad")
newPart.addTag("oompColor", "kicad-footprints")
newPart.addTag("oompDesc", "Capacitor_SMD")
newPart.addTag("oompIndex", "C_1206_3216Metric_Pad1.33x1.80mm_HandSolder")

newPart.addTag("kicadDesc", "Capacitor SMD 1206 (3216 Metric), square (rectangular) end terminal, IPC_7351 nominal with elongated pad for handsoldering. (Body size source: IPC-SM-782 page 76, https://www.pcb-3d.com/wordpress/wp-content/uploads/ipc-sm-782a_amendment_1_and_2.pdf), generated with kicad-footprint-generator")
newPart.addTag("kicadTags", "capacitor handsolder")
newPart.addTag("kicadAttr", "smd")
newPart.addTag("kicad3DModel", "${KICAD6_3DMODEL_DIR}/Capacitor_SMD.3dshapes/C_1206_3216Metric.wrl")

OOMP.parts.append(newPart)