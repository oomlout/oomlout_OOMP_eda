###### OOMP FILE  ######

import OOMP

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "kicad")
newPart.addTag("oompColor", "kicad-footprints")
newPart.addTag("oompDesc", "Package_DFN_QFN")
newPart.addTag("oompIndex", "QFN-12-1EP_3x3mm_P0.5mm_EP1.6x1.6mm_ThermalVias")

newPart.addTag("kicadDesc", "QFN, 12 Pin (https://www.nxp.com/docs/en/data-sheet/MMZ09332B.pdf), generated with kicad-footprint-generator ipc_noLead_generator.py")
newPart.addTag("kicadTags", "QFN NoLead")
newPart.addTag("kicadAttr", "smd")
newPart.addTag("kicad3DModel", "${KICAD6_3DMODEL_DIR}/Package_DFN_QFN.3dshapes/QFN-12-1EP_3x3mm_P0.5mm_EP1.6x1.6mm.wrl")

OOMP.parts.append(newPart)