###### OOMP FILE  ######

import OOMP

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "kicad")
newPart.addTag("oompColor", "kicad-footprints")
newPart.addTag("oompDesc", "Transistor_Power_Module")
newPart.addTag("oompIndex", "Infineon_AG-ECONO2")

newPart.addTag("kicadDesc", "28-lead TH, EconoPACK 2, same as Littelfuse_Package_H_XN2MM, https://www.infineon.com/dgdl/Infineon-FS75R07N2E4-DS-v02_00-en_de.pdf?fileId=db3a30432f5008fe012f52f916333979")
newPart.addTag("kicadTags", "igbt diode module")
newPart.addTag("kicadAttr", "through_hole")
newPart.addTag("kicad3DModel", "${KICAD6_3DMODEL_DIR}/Transistor_Power_Module.3dshapes/Infineon_AG-ECONO2.wrl")

OOMP.parts.append(newPart)