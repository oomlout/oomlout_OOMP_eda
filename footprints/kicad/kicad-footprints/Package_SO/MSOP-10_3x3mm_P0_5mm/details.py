###### OOMP FILE  ######

import OOMP

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "kicad")
newPart.addTag("oompColor", "kicad-footprints")
newPart.addTag("oompDesc", "Package_SO")
newPart.addTag("oompIndex", "MSOP-10_3x3mm_P0.5mm")

newPart.addTag("kicadDesc", "10-Lead Plastic Micro Small Outline Package (MS) [MSOP] (see Microchip Packaging Specification 00000049BS.pdf)")
newPart.addTag("kicadTags", "SSOP 0.5")
newPart.addTag("kicadAttr", "smd")
newPart.addTag("kicad3DModel", "${KICAD6_3DMODEL_DIR}/Package_SO.3dshapes/MSOP-10_3x3mm_P0.5mm.wrl")

OOMP.parts.append(newPart)