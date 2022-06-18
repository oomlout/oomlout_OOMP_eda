###### OOMP FILE  ######

import OOMP

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "kicad")
newPart.addTag("oompColor", "kicad-footprints")
newPart.addTag("oompDesc", "Package_SO")
newPart.addTag("oompIndex", "Linear_MSOP-12-16_3x4mm_P0.5mm")

newPart.addTag("kicadDesc", "12-Lead Plastic Micro Small Outline Package (MS) [MSOP], variant of MSOP-16 (see https://www.analog.com/media/en/technical-documentation/data-sheets/3748fb.pdf)")
newPart.addTag("kicadTags", "SSOP 0.5")
newPart.addTag("kicadAttr", "smd")
newPart.addTag("kicad3DModel", "${KICAD6_3DMODEL_DIR}/Package_SO.3dshapes/Linear_MSOP-12-16_3x4mm_P0.5mm.wrl")

OOMP.parts.append(newPart)