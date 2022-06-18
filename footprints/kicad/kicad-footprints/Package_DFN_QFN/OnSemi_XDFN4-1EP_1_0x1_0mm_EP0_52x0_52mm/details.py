###### OOMP FILE  ######

import OOMP

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "kicad")
newPart.addTag("oompColor", "kicad-footprints")
newPart.addTag("oompDesc", "Package_DFN_QFN")
newPart.addTag("oompIndex", "OnSemi_XDFN4-1EP_1.0x1.0mm_EP0.52x0.52mm")

newPart.addTag("kicadDesc", "XDFN4 footprint (as found on the https://www.onsemi.com/pub/Collateral/NCP115-D.PDF)")
newPart.addTag("kicadTags", "OnSemi XDFN4")
newPart.addTag("kicadAttr", "smd")
newPart.addTag("kicad3DModel", "${KICAD6_3DMODEL_DIR}/Package_DFN_QFN.3dshapes/OnSemi_XDFN4-1EP_1.0x1.0mm_EP0.52x0.52mm.wrl")

OOMP.parts.append(newPart)