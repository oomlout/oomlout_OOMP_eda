###### OOMP FILE  ######

import OOMP

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "kicad")
newPart.addTag("oompColor", "kicad-footprints")
newPart.addTag("oompDesc", "Package_DFN_QFN")
newPart.addTag("oompIndex", "AO_DFN-8-1EP_5.55x5.2mm_P1.27mm_EP4.12x4.6mm")

newPart.addTag("kicadDesc", "DD Package; 8-Lead Plastic DFN (5.55mm x 5.2mm), Pin 5-8 connected to EP (http://www.aosmd.com/res/packaging_information/DFN5x6_8L_EP1_P.pdf)")
newPart.addTag("kicadTags", "dfn")
newPart.addTag("kicadAttr", "smd")
newPart.addTag("kicad3DModel", "${KICAD6_3DMODEL_DIR}/Package_DFN_QFN.3dshapes/AO_DFN-8-1EP_5.55x5.2mm_P1.27mm_EP4.12x4.6mm.wrl")

OOMP.parts.append(newPart)