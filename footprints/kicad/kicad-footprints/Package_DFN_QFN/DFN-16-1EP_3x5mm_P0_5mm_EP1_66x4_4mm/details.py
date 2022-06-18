###### OOMP FILE  ######

import OOMP

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "kicad")
newPart.addTag("oompColor", "kicad-footprints")
newPart.addTag("oompDesc", "Package_DFN_QFN")
newPart.addTag("oompIndex", "DFN-16-1EP_3x5mm_P0.5mm_EP1.66x4.4mm")

newPart.addTag("kicadDesc", "DHC Package; 16-Lead Plastic DFN (5mm x 3mm) (see Linear Technology DFN_16_05-08-1706.pdf)")
newPart.addTag("kicadTags", "DFN 0.5")
newPart.addTag("kicadAttr", "smd")
newPart.addTag("kicad3DModel", "${KICAD6_3DMODEL_DIR}/Package_DFN_QFN.3dshapes/DFN-16-1EP_3x5mm_P0.5mm_EP1.66x4.4mm.wrl")

OOMP.parts.append(newPart)