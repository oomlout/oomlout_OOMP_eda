###### OOMP FILE  ######

import OOMP

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "kicad")
newPart.addTag("oompColor", "kicad-footprints")
newPart.addTag("oompDesc", "Package_DFN_QFN")
newPart.addTag("oompIndex", "TQFN-40-1EP_5x5mm_P0.4mm_EP3.5x3.5mm_ThermalVias")

newPart.addTag("kicadDesc", "TQFN, 40 Pin (https://pdfserv.maximintegrated.com/package_dwgs/21-0140.PDF (T4055-1)), generated with kicad-footprint-generator ipc_noLead_generator.py")
newPart.addTag("kicadTags", "TQFN NoLead")
newPart.addTag("kicadAttr", "smd")
newPart.addTag("kicad3DModel", "${KICAD6_3DMODEL_DIR}/Package_DFN_QFN.3dshapes/TQFN-40-1EP_5x5mm_P0.4mm_EP3.5x3.5mm.wrl")

OOMP.parts.append(newPart)