###### OOMP FILE  ######

import OOMP

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "kicad")
newPart.addTag("oompColor", "kicad-footprints")
newPart.addTag("oompDesc", "Package_DFN_QFN")
newPart.addTag("oompIndex", "QFN-48-1EP_6x6mm_P0.4mm_EP4.6x4.6mm_ThermalVias")

newPart.addTag("kicadDesc", "QFN, 48 Pin (http://infocenter.nordicsemi.com/pdf/nRF51822_PS_v3.3.pdf#page=67), generated with kicad-footprint-generator ipc_noLead_generator.py")
newPart.addTag("kicadTags", "QFN NoLead")
newPart.addTag("kicadAttr", "smd")
newPart.addTag("kicad3DModel", "${KICAD6_3DMODEL_DIR}/Package_DFN_QFN.3dshapes/QFN-48-1EP_6x6mm_P0.4mm_EP4.6x4.6mm.wrl")

OOMP.parts.append(newPart)