###### OOMP FILE  ######

import OOMP

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "kicad")
newPart.addTag("oompColor", "kicad-footprints")
newPart.addTag("oompDesc", "Package_DFN_QFN")
newPart.addTag("oompIndex", "DFN-14-1EP_3x4mm_P0.5mm_EP1.7x3.3mm")

newPart.addTag("kicadDesc", "DE Package; 14-Lead Plastic DFN (4mm x 3mm) (see Linear Technology DFN_14_05-08-1708.pdf)")
newPart.addTag("kicadTags", "DFN 0.5")
newPart.addTag("kicadAttr", "smd")
newPart.addTag("kicad3DModel", "${KICAD6_3DMODEL_DIR}/Package_DFN_QFN.3dshapes/DFN-14-1EP_3x4mm_P0.5mm_EP1.7x3.3mm.wrl")

OOMP.parts.append(newPart)