###### OOMP FILE  ######

import OOMP

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "kicad")
newPart.addTag("oompColor", "kicad-footprints")
newPart.addTag("oompDesc", "Package_DFN_QFN")
newPart.addTag("oompIndex", "UQFN-10_1.3x1.8mm_P0.4mm")

newPart.addTag("kicadDesc", "UQFN, 10 Pin (http://ww1.microchip.com/downloads/en/DeviceDoc/00001725D.pdf (Page 9)), generated with kicad-footprint-generator ipc_noLead_generator.py")
newPart.addTag("kicadTags", "UQFN NoLead")
newPart.addTag("kicadAttr", "smd")
newPart.addTag("kicad3DModel", "${KICAD6_3DMODEL_DIR}/Package_DFN_QFN.3dshapes/UQFN-10_1.3x1.8mm_P0.4mm.wrl")

OOMP.parts.append(newPart)