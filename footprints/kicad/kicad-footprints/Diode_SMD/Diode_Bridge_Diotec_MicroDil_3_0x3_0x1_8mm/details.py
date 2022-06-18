###### OOMP FILE  ######

import OOMP

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "kicad")
newPart.addTag("oompColor", "kicad-footprints")
newPart.addTag("oompDesc", "Diode_SMD")
newPart.addTag("oompIndex", "Diode_Bridge_Diotec_MicroDil_3.0x3.0x1.8mm")

newPart.addTag("kicadDesc", "SMD package Diotec Diotec MicroDil, body 3.0x3.0x1.8mm (e.g. diode bridge), see https://diotec.com/tl_files/diotec/files/pdf/datasheets/mys40.pdf")
newPart.addTag("kicadTags", "Diotec MicroDil diode bridge")
newPart.addTag("kicadAttr", "smd")
newPart.addTag("kicad3DModel", "${KICAD6_3DMODEL_DIR}/Diode_SMD.3dshapes/Diode_Bridge_Diotec_MicroDil_3.0x3.0x1.8mm.wrl")

OOMP.parts.append(newPart)