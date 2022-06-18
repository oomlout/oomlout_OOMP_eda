###### OOMP FILE  ######

import OOMP

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "kicad")
newPart.addTag("oompColor", "kicad-footprints")
newPart.addTag("oompDesc", "Package_DFN_QFN")
newPart.addTag("oompIndex", "QFN-32-1EP_7x7mm_P0.65mm_EP5.4x5.4mm_ThermalVias")

newPart.addTag("kicadDesc", "QFN, 32 Pin (http://www.thatcorp.com/datashts/THAT_5171_Datasheet.pdf), generated with kicad-footprint-generator ipc_noLead_generator.py")
newPart.addTag("kicadTags", "QFN NoLead")
newPart.addTag("kicadAttr", "smd")
newPart.addTag("kicad3DModel", "${KICAD6_3DMODEL_DIR}/Package_DFN_QFN.3dshapes/QFN-32-1EP_7x7mm_P0.65mm_EP5.4x5.4mm.wrl")

OOMP.parts.append(newPart)