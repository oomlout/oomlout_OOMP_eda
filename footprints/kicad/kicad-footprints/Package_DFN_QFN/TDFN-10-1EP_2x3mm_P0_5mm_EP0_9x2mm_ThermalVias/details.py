###### OOMP FILE  ######

import OOMP

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "kicad")
newPart.addTag("oompColor", "kicad-footprints")
newPart.addTag("oompDesc", "Package_DFN_QFN")
newPart.addTag("oompIndex", "TDFN-10-1EP_2x3mm_P0.5mm_EP0.9x2mm_ThermalVias")

newPart.addTag("kicadDesc", "TDFN, 10 Pin (https://pdfserv.maximintegrated.com/package_dwgs/21-0429.PDF), generated with kicad-footprint-generator ipc_noLead_generator.py")
newPart.addTag("kicadTags", "TDFN NoLead")
newPart.addTag("kicadAttr", "smd")
newPart.addTag("kicad3DModel", "${KICAD6_3DMODEL_DIR}/Package_DFN_QFN.3dshapes/TDFN-10-1EP_2x3mm_P0.5mm_EP0.9x2mm.wrl")

OOMP.parts.append(newPart)