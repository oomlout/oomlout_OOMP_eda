###### OOMP FILE  ######

import OOMP

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "kicad")
newPart.addTag("oompColor", "kicad-footprints")
newPart.addTag("oompDesc", "Package_QFP")
newPart.addTag("oompIndex", "TQFP-64-1EP_10x10mm_P0.5mm_EP8x8mm")

newPart.addTag("kicadDesc", "64-Lead Plastic Thin Quad Flatpack (PT) - 10x10x1 mm Body, 2.00 mm Footprint [TQFP] thermal pad")
newPart.addTag("kicadTags", "QFP 0.5")
newPart.addTag("kicadAttr", "smd")
newPart.addTag("kicad3DModel", "${KICAD6_3DMODEL_DIR}/Package_QFP.3dshapes/TQFP-64_10x10mm_P0.5mm_EP8x8mm.wrl")

OOMP.parts.append(newPart)