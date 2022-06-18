###### OOMP FILE  ######

import OOMP

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "kicad")
newPart.addTag("oompColor", "kicad-footprints")
newPart.addTag("oompDesc", "Package_DFN_QFN")
newPart.addTag("oompIndex", "HVQFN-16-1EP_3x3mm_P0.5mm_EP1.5x1.5mm")

newPart.addTag("kicadDesc", "HVQFN, 16 Pin (https://www.nxp.com/docs/en/package-information/SOT758-1.pdf), generated with kicad-footprint-generator ipc_noLead_generator.py")
newPart.addTag("kicadTags", "HVQFN NoLead")
newPart.addTag("kicadAttr", "smd")
newPart.addTag("kicad3DModel", "${KICAD6_3DMODEL_DIR}/Package_DFN_QFN.3dshapes/HVQFN-16-1EP_3x3mm_P0.5mm_EP1.5x1.5mm.wrl")

OOMP.parts.append(newPart)