###### OOMP FILE  ######

import OOMP

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "kicad")
newPart.addTag("oompColor", "kicad-footprints")
newPart.addTag("oompDesc", "Package_DFN_QFN")
newPart.addTag("oompIndex", "QFN-64-1EP_9x9mm_P0.5mm_EP5.45x5.45mm")

newPart.addTag("kicadDesc", "QFN, 64 Pin (https://www.infineon.com/dgdl/Infineon-MA12040-DS-v01_00-EN.pdf?fileId=5546d46264a8de7e0164b7467a3d617c#page=81), generated with kicad-footprint-generator ipc_noLead_generator.py")
newPart.addTag("kicadTags", "QFN NoLead")
newPart.addTag("kicadAttr", "smd")
newPart.addTag("kicad3DModel", "${KICAD6_3DMODEL_DIR}/Package_DFN_QFN.3dshapes/QFN-64-1EP_9x9mm_P0.5mm_EP5.45x5.45mm.wrl")

OOMP.parts.append(newPart)