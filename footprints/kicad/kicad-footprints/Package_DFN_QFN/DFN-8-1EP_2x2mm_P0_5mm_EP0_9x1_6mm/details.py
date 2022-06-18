###### OOMP FILE  ######

import OOMP

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "kicad")
newPart.addTag("oompColor", "kicad-footprints")
newPart.addTag("oompDesc", "Package_DFN_QFN")
newPart.addTag("oompIndex", "DFN-8-1EP_2x2mm_P0.5mm_EP0.9x1.6mm")

newPart.addTag("kicadDesc", "DFN, 8 Pin (https://www.st.com/resource/en/datasheet/lm2903.pdf#page=16), generated with kicad-footprint-generator ipc_noLead_generator.py")
newPart.addTag("kicadTags", "DFN NoLead")
newPart.addTag("kicadAttr", "smd")
newPart.addTag("kicad3DModel", "${KICAD6_3DMODEL_DIR}/Package_DFN_QFN.3dshapes/DFN-8-1EP_2x2mm_P0.5mm_EP0.9x1.6mm.wrl")

OOMP.parts.append(newPart)