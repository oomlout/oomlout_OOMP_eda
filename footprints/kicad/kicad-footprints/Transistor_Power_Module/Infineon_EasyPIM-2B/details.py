###### OOMP FILE  ######

import OOMP

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "kicad")
newPart.addTag("oompColor", "kicad-footprints")
newPart.addTag("oompDesc", "Transistor_Power_Module")
newPart.addTag("oompIndex", "Infineon_EasyPIM-2B")

newPart.addTag("kicadDesc", "35-lead TH, EasyPIM 2B, same as ST_ACEPACK-2-CIB, https://www.infineon.com/dgdl/Infineon-FP50R06W2E3-DS-v02_02-EN.pdf?fileId=db3a30431b3e89eb011b455c99987d24")
newPart.addTag("kicadTags", "brifge rectifier igbt diode module")
newPart.addTag("kicadAttr", "through_hole")
newPart.addTag("kicad3DModel", "${KICAD6_3DMODEL_DIR}/Transistor_Power_Module.3dshapes/Infineon_EasyPIM-2B.wrl")

OOMP.parts.append(newPart)