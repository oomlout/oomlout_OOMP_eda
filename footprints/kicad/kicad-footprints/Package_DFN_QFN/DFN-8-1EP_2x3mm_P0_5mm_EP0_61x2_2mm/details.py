###### OOMP FILE  ######

import OOMP

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "kicad")
newPart.addTag("oompColor", "kicad-footprints")
newPart.addTag("oompDesc", "Package_DFN_QFN")
newPart.addTag("oompIndex", "DFN-8-1EP_2x3mm_P0.5mm_EP0.61x2.2mm")

newPart.addTag("kicadDesc", "DDB Package; 8-Lead Plastic DFN (3mm x 2mm) (see Linear Technology DFN_8_05-08-1702.pdf)")
newPart.addTag("kicadTags", "DFN 0.5")
newPart.addTag("kicadAttr", "smd")
newPart.addTag("kicad3DModel", "${KICAD6_3DMODEL_DIR}/Package_DFN_QFN.3dshapes/DFN-8-1EP_2x3mm_P0.5mm_EP0.61x2.2mm.wrl")

OOMP.parts.append(newPart)