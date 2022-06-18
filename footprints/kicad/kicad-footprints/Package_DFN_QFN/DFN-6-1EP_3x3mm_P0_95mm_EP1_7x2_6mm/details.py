###### OOMP FILE  ######

import OOMP

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "kicad")
newPart.addTag("oompColor", "kicad-footprints")
newPart.addTag("oompDesc", "Package_DFN_QFN")
newPart.addTag("oompIndex", "DFN-6-1EP_3x3mm_P0.95mm_EP1.7x2.6mm")

newPart.addTag("kicadDesc", "DFN6 3*3 MM, 0.95 PITCH; CASE 506AH-01 (see ON Semiconductor 506AH.PDF)")
newPart.addTag("kicadTags", "DFN 0.95")
newPart.addTag("kicadAttr", "smd")
newPart.addTag("kicad3DModel", "${KICAD6_3DMODEL_DIR}/Package_DFN_QFN.3dshapes/DFN-6-1EP_3x3mm_P0.95mm_EP1.7x2.6mm.wrl")

OOMP.parts.append(newPart)