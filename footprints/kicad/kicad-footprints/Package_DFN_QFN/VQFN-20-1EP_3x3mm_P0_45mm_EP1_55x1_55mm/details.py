###### OOMP FILE  ######

import OOMP

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "kicad")
newPart.addTag("oompColor", "kicad-footprints")
newPart.addTag("oompDesc", "Package_DFN_QFN")
newPart.addTag("oompIndex", "VQFN-20-1EP_3x3mm_P0.45mm_EP1.55x1.55mm")

newPart.addTag("kicadDesc", "VQFN, 20 Pin (http://ww1.microchip.com/downloads/en/DeviceDoc/doc8246.pdf#page=264), generated with kicad-footprint-generator ipc_noLead_generator.py")
newPart.addTag("kicadTags", "VQFN NoLead")
newPart.addTag("kicadAttr", "smd")
newPart.addTag("kicad3DModel", "${KICAD6_3DMODEL_DIR}/Package_DFN_QFN.3dshapes/VQFN-20-1EP_3x3mm_P0.45mm_EP1.55x1.55mm.wrl")

OOMP.parts.append(newPart)