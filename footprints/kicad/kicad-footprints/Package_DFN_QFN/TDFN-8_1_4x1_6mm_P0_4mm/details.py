###### OOMP FILE  ######

import OOMP

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "kicad")
newPart.addTag("oompColor", "kicad-footprints")
newPart.addTag("oompDesc", "Package_DFN_QFN")
newPart.addTag("oompIndex", "TDFN-8_1.4x1.6mm_P0.4mm")

newPart.addTag("kicadDesc", "TDFN, 8 Pin (https://www.silabs.com/documents/public/data-sheets/si7210-datasheet.pdf), generated with kicad-footprint-generator ipc_noLead_generator.py")
newPart.addTag("kicadTags", "TDFN NoLead")
newPart.addTag("kicadAttr", "smd")
newPart.addTag("kicad3DModel", "${KICAD6_3DMODEL_DIR}/Package_DFN_QFN.3dshapes/TDFN-8_1.4x1.6mm_P0.4mm.wrl")

OOMP.parts.append(newPart)