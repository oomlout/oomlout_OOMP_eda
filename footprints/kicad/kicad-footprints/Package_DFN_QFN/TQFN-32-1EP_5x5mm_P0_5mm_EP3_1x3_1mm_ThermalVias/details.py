###### OOMP FILE  ######

import OOMP

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "kicad")
newPart.addTag("oompColor", "kicad-footprints")
newPart.addTag("oompDesc", "Package_DFN_QFN")
newPart.addTag("oompIndex", "TQFN-32-1EP_5x5mm_P0.5mm_EP3.1x3.1mm_ThermalVias")

newPart.addTag("kicadDesc", "TQFN, 32 Pin (https://pdfserv.maximintegrated.com/package_dwgs/21-0140.PDF (T3255-3)), generated with kicad-footprint-generator ipc_noLead_generator.py")
newPart.addTag("kicadTags", "TQFN NoLead")
newPart.addTag("kicadAttr", "smd")
newPart.addTag("kicad3DModel", "${KICAD6_3DMODEL_DIR}/Package_DFN_QFN.3dshapes/TQFN-32-1EP_5x5mm_P0.5mm_EP3.1x3.1mm.wrl")

OOMP.parts.append(newPart)