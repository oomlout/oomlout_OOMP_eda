###### OOMP FILE  ######

import OOMP

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "kicad")
newPart.addTag("oompColor", "kicad-footprints")
newPart.addTag("oompDesc", "Package_DFN_QFN")
newPart.addTag("oompIndex", "WQFN-16-1EP_4x4mm_P0.5mm_EP2.6x2.6mm")

newPart.addTag("kicadDesc", "WQFN, 16 Pin (http://www.ti.com/lit/ds/symlink/ldc1312.pdf#page=59), generated with kicad-footprint-generator ipc_noLead_generator.py")
newPart.addTag("kicadTags", "WQFN NoLead")
newPart.addTag("kicadAttr", "smd")
newPart.addTag("kicad3DModel", "${KICAD6_3DMODEL_DIR}/Package_DFN_QFN.3dshapes/WQFN-16-1EP_4x4mm_P0.5mm_EP2.6x2.6mm.wrl")

OOMP.parts.append(newPart)