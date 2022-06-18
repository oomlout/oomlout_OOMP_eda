###### OOMP FILE  ######

import OOMP

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "kicad")
newPart.addTag("oompColor", "kicad-footprints")
newPart.addTag("oompDesc", "Package_DFN_QFN")
newPart.addTag("oompIndex", "QFN-32-1EP_4x4mm_P0.4mm_EP2.65x2.65mm")

newPart.addTag("kicadDesc", "QFN, 32 Pin (https://www.renesas.com/eu/en/package-image/pdf/outdrawing/l32.4x4a.pdf), generated with kicad-footprint-generator ipc_noLead_generator.py")
newPart.addTag("kicadTags", "QFN NoLead")
newPart.addTag("kicadAttr", "smd")
newPart.addTag("kicad3DModel", "${KICAD6_3DMODEL_DIR}/Package_DFN_QFN.3dshapes/QFN-32-1EP_4x4mm_P0.4mm_EP2.65x2.65mm.wrl")

OOMP.parts.append(newPart)