###### OOMP FILE  ######

import OOMP

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "kicad")
newPart.addTag("oompColor", "kicad-footprints")
newPart.addTag("oompDesc", "Package_DFN_QFN")
newPart.addTag("oompIndex", "QFN-20-1EP_3.5x3.5mm_P0.5mm_EP2x2mm_ThermalVias")

newPart.addTag("kicadDesc", "QFN, 20 Pin (http://www.ti.com/lit/ml/mpqf239/mpqf239.pdf), generated with kicad-footprint-generator ipc_noLead_generator.py")
newPart.addTag("kicadTags", "QFN NoLead")
newPart.addTag("kicadAttr", "smd")
newPart.addTag("kicad3DModel", "${KICAD6_3DMODEL_DIR}/Package_DFN_QFN.3dshapes/QFN-20-1EP_3.5x3.5mm_P0.5mm_EP2x2mm.wrl")

OOMP.parts.append(newPart)