###### OOMP FILE  ######

import OOMP

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "kicad")
newPart.addTag("oompColor", "kicad-footprints")
newPart.addTag("oompDesc", "Package_DFN_QFN")
newPart.addTag("oompIndex", "OnSemi_UDFN-8_1.2x1.8mm_P0.4mm")

newPart.addTag("kicadDesc", "8-Lead Plastic Dual Flat, No Lead Package, 1.2x1.8x1.55 mm Body [UDFN] (See http://www.onsemi.com/pub/Collateral/NLSV2T244-D.PDF)")
newPart.addTag("kicadTags", "dfn udfn dual flat")
newPart.addTag("kicadAttr", "smd")
newPart.addTag("kicad3DModel", "${KICAD6_3DMODEL_DIR}/Package_DFN_QFN.3dshapes/OnSemi_UDFN-8_1.2x1.8mm_P0.4mm.wrl")

OOMP.parts.append(newPart)