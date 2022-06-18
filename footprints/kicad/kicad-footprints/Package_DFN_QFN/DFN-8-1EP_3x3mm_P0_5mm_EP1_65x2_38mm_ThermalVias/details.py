###### OOMP FILE  ######

import OOMP

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "kicad")
newPart.addTag("oompColor", "kicad-footprints")
newPart.addTag("oompDesc", "Package_DFN_QFN")
newPart.addTag("oompIndex", "DFN-8-1EP_3x3mm_P0.5mm_EP1.65x2.38mm_ThermalVias")

newPart.addTag("kicadDesc", "DFN, 8 Pin (https://www.analog.com/media/en/technical-documentation/data-sheets/4320fb.pdf), generated with kicad-footprint-generator ipc_noLead_generator.py")
newPart.addTag("kicadTags", "DFN NoLead")
newPart.addTag("kicadAttr", "smd")
newPart.addTag("kicad3DModel", "${KICAD6_3DMODEL_DIR}/Package_DFN_QFN.3dshapes/DFN-8-1EP_3x3mm_P0.5mm_EP1.65x2.38mm.wrl")

OOMP.parts.append(newPart)