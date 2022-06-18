###### OOMP FILE  ######

import OOMP

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "kicad")
newPart.addTag("oompColor", "kicad-footprints")
newPart.addTag("oompDesc", "Package_DFN_QFN")
newPart.addTag("oompIndex", "QFN-36-1EP_6x6mm_P0.5mm_EP3.7x3.7mm")

newPart.addTag("kicadDesc", "QFN, 36 Pin (http://ww1.microchip.com/downloads/en/DeviceDoc/36L_QFN_6x6_with_3_7x3_7_EP_Punch_Dimpled_4E_C04-0241A.pdf), generated with kicad-footprint-generator ipc_noLead_generator.py")
newPart.addTag("kicadTags", "QFN NoLead")
newPart.addTag("kicadAttr", "smd")
newPart.addTag("kicad3DModel", "${KICAD6_3DMODEL_DIR}/Package_DFN_QFN.3dshapes/QFN-36-1EP_6x6mm_P0.5mm_EP3.7x3.7mm.wrl")

OOMP.parts.append(newPart)