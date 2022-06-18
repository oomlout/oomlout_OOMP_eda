###### OOMP FILE  ######

import OOMP

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "kicad")
newPart.addTag("oompColor", "kicad-footprints")
newPart.addTag("oompDesc", "Package_DFN_QFN")
newPart.addTag("oompIndex", "QFN-20-1EP_4x4mm_P0.5mm_EP2.5x2.5mm_ThermalVias")

newPart.addTag("kicadDesc", "QFN, 20 Pin (http://ww1.microchip.com/downloads/en/PackagingSpec/00000049BQ.pdf#page=274), generated with kicad-footprint-generator ipc_noLead_generator.py")
newPart.addTag("kicadTags", "QFN NoLead")
newPart.addTag("kicadAttr", "smd")
newPart.addTag("kicad3DModel", "${KICAD6_3DMODEL_DIR}/Package_DFN_QFN.3dshapes/QFN-20-1EP_4x4mm_P0.5mm_EP2.5x2.5mm.wrl")

OOMP.parts.append(newPart)