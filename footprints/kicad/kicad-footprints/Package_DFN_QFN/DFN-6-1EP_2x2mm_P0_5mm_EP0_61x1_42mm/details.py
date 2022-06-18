###### OOMP FILE  ######

import OOMP

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "kicad")
newPart.addTag("oompColor", "kicad-footprints")
newPart.addTag("oompDesc", "Package_DFN_QFN")
newPart.addTag("oompIndex", "DFN-6-1EP_2x2mm_P0.5mm_EP0.61x1.42mm")

newPart.addTag("kicadDesc", "DC6 Package; 6-Lead Plastic DFN (2mm x 2mm) (see Linear Technology DFN_6_05-08-1703.pdf)")
newPart.addTag("kicadTags", "DFN 0.5")
newPart.addTag("kicadAttr", "smd")
newPart.addTag("kicad3DModel", "${KICAD6_3DMODEL_DIR}/Package_DFN_QFN.3dshapes/DFN-6-1EP_2x2mm_P0.5mm_EP0.61x1.42mm.wrl")

OOMP.parts.append(newPart)