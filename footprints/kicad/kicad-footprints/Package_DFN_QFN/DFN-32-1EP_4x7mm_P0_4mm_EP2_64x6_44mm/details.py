###### OOMP FILE  ######

import OOMP

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "kicad")
newPart.addTag("oompColor", "kicad-footprints")
newPart.addTag("oompDesc", "Package_DFN_QFN")
newPart.addTag("oompIndex", "DFN-32-1EP_4x7mm_P0.4mm_EP2.64x6.44mm")

newPart.addTag("kicadDesc", "DKD Package; 32-Lead Plastic DFN (7mm x 4mm) (see Linear Technology DFN_32_05-08-1734.pdf)")
newPart.addTag("kicadTags", "DFN 0.4")
newPart.addTag("kicadAttr", "smd")
newPart.addTag("kicad3DModel", "${KICAD6_3DMODEL_DIR}/Package_DFN_QFN.3dshapes/DFN-32-1EP_4x7mm_P0.4mm_EP2.64x6.44mm.wrl")

OOMP.parts.append(newPart)