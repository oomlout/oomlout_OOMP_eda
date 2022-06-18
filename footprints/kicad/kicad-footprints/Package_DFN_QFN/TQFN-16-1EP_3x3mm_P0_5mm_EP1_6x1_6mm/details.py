###### OOMP FILE  ######

import OOMP

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "kicad")
newPart.addTag("oompColor", "kicad-footprints")
newPart.addTag("oompDesc", "Package_DFN_QFN")
newPart.addTag("oompIndex", "TQFN-16-1EP_3x3mm_P0.5mm_EP1.6x1.6mm")

newPart.addTag("kicadDesc", "TQFN, 16 Pin (https://www.diodes.com/assets/Datasheets/PI6C5946002.pdf#page=12), generated with kicad-footprint-generator ipc_noLead_generator.py")
newPart.addTag("kicadTags", "TQFN NoLead")
newPart.addTag("kicadAttr", "smd")
newPart.addTag("kicad3DModel", "${KICAD6_3DMODEL_DIR}/Package_DFN_QFN.3dshapes/TQFN-16-1EP_3x3mm_P0.5mm_EP1.6x1.6mm.wrl")

OOMP.parts.append(newPart)