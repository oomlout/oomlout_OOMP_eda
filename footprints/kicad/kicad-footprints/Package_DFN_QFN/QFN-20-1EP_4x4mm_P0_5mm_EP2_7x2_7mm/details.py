###### OOMP FILE  ######

import OOMP

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "kicad")
newPart.addTag("oompColor", "kicad-footprints")
newPart.addTag("oompDesc", "Package_DFN_QFN")
newPart.addTag("oompIndex", "QFN-20-1EP_4x4mm_P0.5mm_EP2.7x2.7mm")

newPart.addTag("kicadDesc", "QFN, 20 Pin (https://www.silabs.com/documents/public/data-sheets/Si5351-B.pdf), generated with kicad-footprint-generator ipc_noLead_generator.py")
newPart.addTag("kicadTags", "QFN NoLead")
newPart.addTag("kicadAttr", "smd")
newPart.addTag("kicad3DModel", "${KICAD6_3DMODEL_DIR}/Package_DFN_QFN.3dshapes/QFN-20-1EP_4x4mm_P0.5mm_EP2.7x2.7mm.wrl")

OOMP.parts.append(newPart)