###### OOMP FILE  ######

import OOMP

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "kicad")
newPart.addTag("oompColor", "kicad-footprints")
newPart.addTag("oompDesc", "Package_DFN_QFN")
newPart.addTag("oompIndex", "WDFN-12-1EP_3x3mm_P0.45mm_EP1.7x2.5mm")

newPart.addTag("kicadDesc", "WDFN, 12 Pin (https://www.diodes.com/assets/Datasheets/PAM2306.pdf), generated with kicad-footprint-generator ipc_noLead_generator.py")
newPart.addTag("kicadTags", "WDFN NoLead")
newPart.addTag("kicadAttr", "smd")
newPart.addTag("kicad3DModel", "${KICAD6_3DMODEL_DIR}/Package_DFN_QFN.3dshapes/WDFN-12-1EP_3x3mm_P0.45mm_EP1.7x2.5mm.wrl")

OOMP.parts.append(newPart)