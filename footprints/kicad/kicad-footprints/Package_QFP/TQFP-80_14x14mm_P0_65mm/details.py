###### OOMP FILE  ######

import OOMP

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "kicad")
newPart.addTag("oompColor", "kicad-footprints")
newPart.addTag("oompDesc", "Package_QFP")
newPart.addTag("oompIndex", "TQFP-80_14x14mm_P0.65mm")

newPart.addTag("kicadDesc", "80-Lead Plastic Thin Quad Flatpack (PF) - 14x14x1 mm Body, 2.00 mm [TQFP] (see Microchip Packaging Specification 00000049BS.pdf)")
newPart.addTag("kicadTags", "QFP 0.65")
newPart.addTag("kicadAttr", "smd")
newPart.addTag("kicad3DModel", "${KICAD6_3DMODEL_DIR}/Package_QFP.3dshapes/TQFP-80_14x14mm_P0.65mm.wrl")

OOMP.parts.append(newPart)