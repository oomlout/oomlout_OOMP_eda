###### OOMP FILE  ######

import OOMP

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "kicad")
newPart.addTag("oompColor", "kicad-footprints")
newPart.addTag("oompDesc", "Package_DFN_QFN")
newPart.addTag("oompIndex", "QFN-20-1EP_3x3mm_P0.4mm_EP1.65x1.65mm_ThermalVias")

newPart.addTag("kicadDesc", "QFN, 20 Pin (https://www.analog.com/media/en/technical-documentation/data-sheets/3553fc.pdf#page=34), generated with kicad-footprint-generator ipc_noLead_generator.py")
newPart.addTag("kicadTags", "QFN NoLead")
newPart.addTag("kicadAttr", "smd")
newPart.addTag("kicad3DModel", "${KICAD6_3DMODEL_DIR}/Package_DFN_QFN.3dshapes/QFN-20-1EP_3x3mm_P0.4mm_EP1.65x1.65mm.wrl")

OOMP.parts.append(newPart)