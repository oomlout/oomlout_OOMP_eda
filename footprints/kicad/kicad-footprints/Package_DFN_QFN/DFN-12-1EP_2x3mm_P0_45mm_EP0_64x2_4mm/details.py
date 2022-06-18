###### OOMP FILE  ######

import OOMP

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "kicad")
newPart.addTag("oompColor", "kicad-footprints")
newPart.addTag("oompDesc", "Package_DFN_QFN")
newPart.addTag("oompIndex", "DFN-12-1EP_2x3mm_P0.45mm_EP0.64x2.4mm")

newPart.addTag("kicadDesc", "DDB Package; 12-Lead Plastic DFN (3mm x 2mm) (see Linear Technology DFN_12_05-08-1723.pdf)")
newPart.addTag("kicadTags", "DFN 0.45")
newPart.addTag("kicadAttr", "smd")
newPart.addTag("kicad3DModel", "${KICAD6_3DMODEL_DIR}/Package_DFN_QFN.3dshapes/DFN-12-1EP_2x3mm_P0.45mm_EP0.64x2.4mm.wrl")

OOMP.parts.append(newPart)