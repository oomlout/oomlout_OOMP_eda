###### OOMP FILE  ######

import OOMP

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "kicad")
newPart.addTag("oompColor", "kicad-footprints")
newPart.addTag("oompDesc", "Package_DFN_QFN")
newPart.addTag("oompIndex", "DFN-8-1EP_6x5mm_P1.27mm_EP4x4mm")

newPart.addTag("kicadDesc", "DD Package; 8-Lead Plastic DFN (6mm x 5mm) (see http://www.everspin.com/file/236/download)")
newPart.addTag("kicadTags", "dfn")
newPart.addTag("kicadAttr", "smd")
newPart.addTag("kicad3DModel", "${KICAD6_3DMODEL_DIR}/Package_DFN_QFN.3dshapes/DFN-8-1EP_6x5mm_Pitch1.27mm.wrl")

OOMP.parts.append(newPart)