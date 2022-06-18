###### OOMP FILE  ######

import OOMP

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "kicad")
newPart.addTag("oompColor", "kicad-footprints")
newPart.addTag("oompDesc", "Package_DFN_QFN")
newPart.addTag("oompIndex", "QFN-16-1EP_5x5mm_P0.8mm_EP2.7x2.7mm_ThermalVias")

newPart.addTag("kicadDesc", "QFN, 16 Pin (http://www.intersil.com/content/dam/Intersil/documents/l16_/l16.5x5.pdf), generated with kicad-footprint-generator ipc_noLead_generator.py")
newPart.addTag("kicadTags", "QFN NoLead")
newPart.addTag("kicadAttr", "smd")
newPart.addTag("kicad3DModel", "${KICAD6_3DMODEL_DIR}/Package_DFN_QFN.3dshapes/QFN-16-1EP_5x5mm_P0.8mm_EP2.7x2.7mm.wrl")

OOMP.parts.append(newPart)