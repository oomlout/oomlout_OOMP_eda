###### OOMP FILE  ######

import OOMP

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "kicad")
newPart.addTag("oompColor", "kicad-footprints")
newPart.addTag("oompDesc", "Package_DFN_QFN")
newPart.addTag("oompIndex", "Qorvo_DFN-8-1EP_2x2mm_P0.5mm")

newPart.addTag("kicadDesc", "DFN 8 2x2mm, 0.5mm http://www.qorvo.com/products/d/da000896")
newPart.addTag("kicadTags", "DFN 0.5 Qorvo 2x2mm")
newPart.addTag("kicadAttr", "smd")
newPart.addTag("kicad3DModel", "${KICAD6_3DMODEL_DIR}/Package_DFN_QFN.3dshapes/Qorvo_DFN-8-1EP_2x2mm_P0.5mm.wrl")

OOMP.parts.append(newPart)