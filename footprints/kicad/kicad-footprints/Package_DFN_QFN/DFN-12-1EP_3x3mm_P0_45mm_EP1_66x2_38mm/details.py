###### OOMP FILE  ######

import OOMP

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "kicad")
newPart.addTag("oompColor", "kicad-footprints")
newPart.addTag("oompDesc", "Package_DFN_QFN")
newPart.addTag("oompIndex", "DFN-12-1EP_3x3mm_P0.45mm_EP1.66x2.38mm")

newPart.addTag("kicadDesc", "DD Package; 12-Lead Plastic DFN (3mm x 3mm) (see Linear Technology DFN_12_05-08-1725.pdf)")
newPart.addTag("kicadTags", "DFN 0.45")
newPart.addTag("kicadAttr", "smd")
newPart.addTag("kicad3DModel", "${KICAD6_3DMODEL_DIR}/Package_DFN_QFN.3dshapes/DFN-12-1EP_3x3mm_P0.45mm_EP1.66x2.38mm.wrl")

OOMP.parts.append(newPart)