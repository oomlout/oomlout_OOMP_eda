###### OOMP FILE  ######

import OOMP

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "kicad")
newPart.addTag("oompColor", "kicad-footprints")
newPart.addTag("oompDesc", "Diode_SMD")
newPart.addTag("oompIndex", "Diode_Bridge_Diotec_ABS")

newPart.addTag("kicadDesc", "SMD diode bridge ABS (Diotec), see https://diotec.com/tl_files/diotec/files/pdf/datasheets/abs2.pdf")
newPart.addTag("kicadTags", "ABS MBLS")
newPart.addTag("kicadAttr", "smd")
newPart.addTag("kicad3DModel", "${KICAD6_3DMODEL_DIR}/Diode_SMD.3dshapes/Diode_Bridge_Diotec_ABS.wrl")

OOMP.parts.append(newPart)