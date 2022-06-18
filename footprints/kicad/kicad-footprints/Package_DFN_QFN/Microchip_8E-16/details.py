###### OOMP FILE  ######

import OOMP

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "kicad")
newPart.addTag("oompColor", "kicad-footprints")
newPart.addTag("oompDesc", "Package_DFN_QFN")
newPart.addTag("oompIndex", "Microchip_8E-16")

newPart.addTag("kicadDesc", "16-Lead Quad Flat, No Lead Package (8E) - 4x4x0.9 mm Body [UQFN]; (see Microchip Packaging Specification 00000049BS.pdf)")
newPart.addTag("kicadTags", "QFN Microchip 8E 16")
newPart.addTag("kicadAttr", "smd")
newPart.addTag("kicad3DModel", "${KICAD6_3DMODEL_DIR}/Package_DFN_QFN.3dshapes/QFN-16-1EP_4x4mm_Pitch0.65mm.wrl")

OOMP.parts.append(newPart)