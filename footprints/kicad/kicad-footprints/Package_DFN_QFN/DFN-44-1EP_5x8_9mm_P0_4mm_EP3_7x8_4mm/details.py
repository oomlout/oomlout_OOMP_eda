###### OOMP FILE  ######

import OOMP

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "kicad")
newPart.addTag("oompColor", "kicad-footprints")
newPart.addTag("oompDesc", "Package_DFN_QFN")
newPart.addTag("oompIndex", "DFN-44-1EP_5x8.9mm_P0.4mm_EP3.7x8.4mm")

newPart.addTag("kicadDesc", "DFN44 8.9x5, 0.4P; CASE 506BU-01 (see ON Semiconductor 506BU.PDF)")
newPart.addTag("kicadTags", "DFN 0.4")
newPart.addTag("kicadAttr", "smd")
newPart.addTag("kicad3DModel", "${KICAD6_3DMODEL_DIR}/Package_DFN_QFN.3dshapes/DFN-44-1EP_5x8.9mm_P0.4mm_EP3.7x8.4mm.wrl")

OOMP.parts.append(newPart)