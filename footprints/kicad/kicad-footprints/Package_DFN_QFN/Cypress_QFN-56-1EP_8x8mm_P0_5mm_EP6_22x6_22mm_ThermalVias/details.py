###### OOMP FILE  ######

import OOMP

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "kicad")
newPart.addTag("oompColor", "kicad-footprints")
newPart.addTag("oompDesc", "Package_DFN_QFN")
newPart.addTag("oompIndex", "Cypress_QFN-56-1EP_8x8mm_P0.5mm_EP6.22x6.22mm_ThermalVias")

newPart.addTag("kicadDesc", "56-Lead Plastic Quad Flat, No Lead Package (ML) - 8x8x0.9 mm Body [QFN] (see datasheet at http://www.cypress.com/file/138911/download and app note at http://www.cypress.com/file/140006/download)")
newPart.addTag("kicadTags", "QFN 0.5")
newPart.addTag("kicadAttr", "smd")
newPart.addTag("kicad3DModel", "${KICAD6_3DMODEL_DIR}/Package_DFN_QFN.3dshapes/QFN-56-1EP_8x8mm_P0.5mm_EP6.22x6.22mm_ThermalVias.wrl")

OOMP.parts.append(newPart)