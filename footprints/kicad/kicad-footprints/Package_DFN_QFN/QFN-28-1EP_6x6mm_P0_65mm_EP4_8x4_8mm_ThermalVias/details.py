###### OOMP FILE  ######

import OOMP

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "kicad")
newPart.addTag("oompColor", "kicad-footprints")
newPart.addTag("oompDesc", "Package_DFN_QFN")
newPart.addTag("oompIndex", "QFN-28-1EP_6x6mm_P0.65mm_EP4.8x4.8mm_ThermalVias")

newPart.addTag("kicadDesc", "QFN, 28 Pin (https://www.semtech.com/uploads/documents/sx1272.pdf#page=125), generated with kicad-footprint-generator ipc_noLead_generator.py")
newPart.addTag("kicadTags", "QFN NoLead")
newPart.addTag("kicadAttr", "smd")
newPart.addTag("kicad3DModel", "${KICAD6_3DMODEL_DIR}/Package_DFN_QFN.3dshapes/QFN-28-1EP_6x6mm_P0.65mm_EP4.8x4.8mm.wrl")

OOMP.parts.append(newPart)