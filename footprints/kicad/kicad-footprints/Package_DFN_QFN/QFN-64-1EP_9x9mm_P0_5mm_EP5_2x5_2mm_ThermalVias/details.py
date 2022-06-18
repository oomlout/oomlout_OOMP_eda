###### OOMP FILE  ######

import OOMP

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "kicad")
newPart.addTag("oompColor", "kicad-footprints")
newPart.addTag("oompDesc", "Package_DFN_QFN")
newPart.addTag("oompIndex", "QFN-64-1EP_9x9mm_P0.5mm_EP5.2x5.2mm_ThermalVias")

newPart.addTag("kicadDesc", "QFN, 64 Pin (https://www.silabs.com/documents/public/data-sheets/Si5345-44-42-D-DataSheet.pdf#page=51), generated with kicad-footprint-generator ipc_noLead_generator.py")
newPart.addTag("kicadTags", "QFN NoLead")
newPart.addTag("kicadAttr", "smd")
newPart.addTag("kicad3DModel", "${KICAD6_3DMODEL_DIR}/Package_DFN_QFN.3dshapes/QFN-64-1EP_9x9mm_P0.5mm_EP5.2x5.2mm.wrl")

OOMP.parts.append(newPart)