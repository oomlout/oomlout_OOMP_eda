###### OOMP FILE  ######

import OOMP

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "kicad")
newPart.addTag("oompColor", "kicad-footprints")
newPart.addTag("oompDesc", "Package_DFN_QFN")
newPart.addTag("oompIndex", "UQFN-16-1EP_3x3mm_P0.5mm_EP1.75x1.75mm")

newPart.addTag("kicadDesc", "16-Lead Ultra Thin Quad Flat, No Lead Package (UC) - 3x3x0.5 mm Body [UQFN]; (see Microchip Packaging Specification 00000049BS.pdf)")
newPart.addTag("kicadTags", "QFN 0.5")
newPart.addTag("kicadAttr", "smd")
newPart.addTag("kicad3DModel", "${KICAD6_3DMODEL_DIR}/Package_DFN_QFN.3dshapes/UQFN-16-1EP_3x3mm_P0.5mm_EP1.75x1.75mm.wrl")

OOMP.parts.append(newPart)