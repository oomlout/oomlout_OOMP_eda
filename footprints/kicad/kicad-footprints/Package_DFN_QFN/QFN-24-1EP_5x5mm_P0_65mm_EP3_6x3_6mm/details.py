###### OOMP FILE  ######

import OOMP

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "kicad")
newPart.addTag("oompColor", "kicad-footprints")
newPart.addTag("oompDesc", "Package_DFN_QFN")
newPart.addTag("oompIndex", "QFN-24-1EP_5x5mm_P0.65mm_EP3.6x3.6mm")

newPart.addTag("kicadDesc", "QFN, 24 Pin (https://www.nxp.com/docs/en/package-information/98ASA00734D.pdf), generated with kicad-footprint-generator ipc_noLead_generator.py")
newPart.addTag("kicadTags", "QFN NoLead")
newPart.addTag("kicadAttr", "smd")
newPart.addTag("kicad3DModel", "${KICAD6_3DMODEL_DIR}/Package_DFN_QFN.3dshapes/QFN-24-1EP_5x5mm_P0.65mm_EP3.6x3.6mm.wrl")

OOMP.parts.append(newPart)