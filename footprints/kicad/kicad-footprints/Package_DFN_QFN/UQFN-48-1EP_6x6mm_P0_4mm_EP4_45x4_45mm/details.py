###### OOMP FILE  ######

import OOMP

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "kicad")
newPart.addTag("oompColor", "kicad-footprints")
newPart.addTag("oompDesc", "Package_DFN_QFN")
newPart.addTag("oompIndex", "UQFN-48-1EP_6x6mm_P0.4mm_EP4.45x4.45mm")

newPart.addTag("kicadDesc", "UQFN, 48 Pin (http://ww1.microchip.com/downloads/en/PackagingSpec/00000049BQ.pdf#page=347), generated with kicad-footprint-generator ipc_noLead_generator.py")
newPart.addTag("kicadTags", "UQFN NoLead")
newPart.addTag("kicadAttr", "smd")
newPart.addTag("kicad3DModel", "${KICAD6_3DMODEL_DIR}/Package_DFN_QFN.3dshapes/UQFN-48-1EP_6x6mm_P0.4mm_EP4.45x4.45mm.wrl")

OOMP.parts.append(newPart)