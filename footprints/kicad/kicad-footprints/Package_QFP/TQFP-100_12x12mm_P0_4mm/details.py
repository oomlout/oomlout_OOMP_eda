###### OOMP FILE  ######

import OOMP

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "kicad")
newPart.addTag("oompColor", "kicad-footprints")
newPart.addTag("oompDesc", "Package_QFP")
newPart.addTag("oompIndex", "TQFP-100_12x12mm_P0.4mm")

newPart.addTag("kicadDesc", "100-Lead Plastic Thin Quad Flatpack (PT) - 12x12x1 mm Body, 2.00 mm [TQFP] (see Microchip Packaging Specification 00000049BS.pdf)")
newPart.addTag("kicadTags", "QFP 0.4")
newPart.addTag("kicadAttr", "smd")
newPart.addTag("kicad3DModel", "${KICAD6_3DMODEL_DIR}/Package_QFP.3dshapes/TQFP-100_12x12mm_P0.4mm.wrl")

OOMP.parts.append(newPart)