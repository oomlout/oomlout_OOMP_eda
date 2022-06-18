###### OOMP FILE  ######

import OOMP

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "kicad")
newPart.addTag("oompColor", "kicad-footprints")
newPart.addTag("oompDesc", "Package_DFN_QFN")
newPart.addTag("oompIndex", "DFN-14-1EP_4x4mm_P0.5mm_EP2.86x3.6mm")

newPart.addTag("kicadDesc", "DFN14, 4x4, 0.5P; CASE 506CM (see ON Semiconductor 506CM.PDF)")
newPart.addTag("kicadTags", "DFN 0.5")
newPart.addTag("kicadAttr", "smd")
newPart.addTag("kicad3DModel", "${KICAD6_3DMODEL_DIR}/Package_DFN_QFN.3dshapes/DFN-14-1EP_4x4mm_P0.5mm_EP2.86x3.6mm.wrl")

OOMP.parts.append(newPart)