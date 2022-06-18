###### OOMP FILE  ######

import OOMP

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "kicad")
newPart.addTag("oompColor", "kicad-footprints")
newPart.addTag("oompDesc", "Package_DFN_QFN")
newPart.addTag("oompIndex", "VQFN-64-1EP_9x9mm_P0.5mm_EP7.15x7.15mm_ThermalVias")

newPart.addTag("kicadDesc", "VQFN, 64 Pin (http://ww1.microchip.com/downloads/en/DeviceDoc/64L_QFN_9x9_MR_C04-00149e.pdf), generated with kicad-footprint-generator ipc_noLead_generator.py")
newPart.addTag("kicadTags", "VQFN NoLead")
newPart.addTag("kicadAttr", "smd")
newPart.addTag("kicad3DModel", "${KICAD6_3DMODEL_DIR}/Package_DFN_QFN.3dshapes/VQFN-64-1EP_9x9mm_P0.5mm_EP7.15x7.15mm.wrl")

OOMP.parts.append(newPart)