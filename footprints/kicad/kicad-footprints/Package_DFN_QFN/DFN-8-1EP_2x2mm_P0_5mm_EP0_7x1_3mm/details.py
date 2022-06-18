###### OOMP FILE  ######

import OOMP

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "kicad")
newPart.addTag("oompColor", "kicad-footprints")
newPart.addTag("oompDesc", "Package_DFN_QFN")
newPart.addTag("oompIndex", "DFN-8-1EP_2x2mm_P0.5mm_EP0.7x1.3mm")

newPart.addTag("kicadDesc", "DFN, 8 Pin (https://www.onsemi.com/pub/Collateral/NUF4401MN-D.PDF#page=6), generated with kicad-footprint-generator ipc_noLead_generator.py")
newPart.addTag("kicadTags", "DFN NoLead")
newPart.addTag("kicadAttr", "smd")
newPart.addTag("kicad3DModel", "${KICAD6_3DMODEL_DIR}/Package_DFN_QFN.3dshapes/DFN-8-1EP_2x2mm_P0.5mm_EP0.7x1.3mm.wrl")

OOMP.parts.append(newPart)