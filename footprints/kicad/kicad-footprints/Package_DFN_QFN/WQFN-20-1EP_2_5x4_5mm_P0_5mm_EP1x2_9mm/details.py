###### OOMP FILE  ######

import OOMP

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "kicad")
newPart.addTag("oompColor", "kicad-footprints")
newPart.addTag("oompDesc", "Package_DFN_QFN")
newPart.addTag("oompIndex", "WQFN-20-1EP_2.5x4.5mm_P0.5mm_EP1x2.9mm")

newPart.addTag("kicadDesc", "http://www.onsemi.com/pub/Collateral/510CD.PDF")
newPart.addTag("kicadTags", "WQFN-20 4.5mm 2.5mm 0.5mm")
newPart.addTag("kicadAttr", "smd")
newPart.addTag("kicad3DModel", "${KICAD6_3DMODEL_DIR}/Package_DFN_QFN.3dshapes/WQFN-20-1EP_2.5x4.5mm_P0.5mm_EP1x2.9mm.wrl")

OOMP.parts.append(newPart)