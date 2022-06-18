###### OOMP FILE  ######

import OOMP

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "kicad")
newPart.addTag("oompColor", "kicad-footprints")
newPart.addTag("oompDesc", "Package_DFN_QFN")
newPart.addTag("oompIndex", "UFQFPN-32-1EP_5x5mm_P0.5mm_EP3.5x3.5mm_ThermalVias")

newPart.addTag("kicadDesc", "UFQFPN, 32 Pin (https://www.st.com/resource/en/datasheet/stm32g071k8.pdf), generated with kicad-footprint-generator ipc_noLead_generator.py")
newPart.addTag("kicadTags", "UFQFPN NoLead")
newPart.addTag("kicadAttr", "smd")
newPart.addTag("kicad3DModel", "${KICAD6_3DMODEL_DIR}/Package_DFN_QFN.3dshapes/UFQFPN-32-1EP_5x5mm_P0.5mm_EP3.5x3.5mm.wrl")

OOMP.parts.append(newPart)