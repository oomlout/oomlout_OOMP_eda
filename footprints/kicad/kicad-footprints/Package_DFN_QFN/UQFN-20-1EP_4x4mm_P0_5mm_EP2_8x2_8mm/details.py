###### OOMP FILE  ######

import OOMP

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "kicad")
newPart.addTag("oompColor", "kicad-footprints")
newPart.addTag("oompDesc", "Package_DFN_QFN")
newPart.addTag("oompIndex", "UQFN-20-1EP_4x4mm_P0.5mm_EP2.8x2.8mm")

newPart.addTag("kicadDesc", "UQFN, 20 Pin (http://ww1.microchip.com/downloads/en/DeviceDoc/40001839B.pdf#page=464), generated with kicad-footprint-generator ipc_noLead_generator.py")
newPart.addTag("kicadTags", "UQFN NoLead")
newPart.addTag("kicadAttr", "smd")
newPart.addTag("kicad3DModel", "${KICAD6_3DMODEL_DIR}/Package_DFN_QFN.3dshapes/UQFN-20-1EP_4x4mm_P0.5mm_EP2.8x2.8mm.wrl")

OOMP.parts.append(newPart)