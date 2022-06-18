###### OOMP FILE  ######

import OOMP

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "kicad")
newPart.addTag("oompColor", "kicad-footprints")
newPart.addTag("oompDesc", "Resistor_SMD")
newPart.addTag("oompIndex", "R_Shunt_Vishay_WSK2512_6332Metric_T1.19mm")

newPart.addTag("kicadDesc", "Shunt Resistor SMD 2512 (6332 Metric), 2.6mm thick, Vishay WKS2512, Terminal length (T) 1.19mm, 5 to 200 milli Ohm (http://http://www.vishay.com/docs/30108/wsk.pdf)")
newPart.addTag("kicadTags", "resistor shunt WSK2512")
newPart.addTag("kicadAttr", "smd")
newPart.addTag("kicad3DModel", "${KICAD6_3DMODEL_DIR}/Resistor_SMD.3dshapes/R_Shunt_Vishay_WSK2512_6332Metric_T1.19mm.wrl")

OOMP.parts.append(newPart)