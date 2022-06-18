###### OOMP FILE  ######

import OOMP

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "kicad")
newPart.addTag("oompColor", "kicad-footprints")
newPart.addTag("oompDesc", "Package_DFN_QFN")
newPart.addTag("oompIndex", "QFN-48-1EP_6x6mm_P0.4mm_EP4.66x4.66mm")

newPart.addTag("kicadDesc", "QFN, 48 Pin (https://www.onsemi.com/pub/Collateral/485BA.PDF), generated with kicad-footprint-generator ipc_noLead_generator.py")
newPart.addTag("kicadTags", "QFN NoLead")
newPart.addTag("kicadAttr", "smd")
newPart.addTag("kicad3DModel", "${KICAD6_3DMODEL_DIR}/Package_DFN_QFN.3dshapes/QFN-48-1EP_6x6mm_P0.4mm_EP4.66x4.66mm.wrl")

OOMP.parts.append(newPart)