###### OOMP FILE  ######

import OOMP

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "kicad")
newPart.addTag("oompColor", "kicad-footprints")
newPart.addTag("oompDesc", "Package_BGA")
newPart.addTag("oompIndex", "UFBGA-32_4.0x4.0mm_Layout6x6_P0.5mm")

newPart.addTag("kicadDesc", "UFBGA-32, 6x6, 4x4mm package, pitch 0.5mm")
newPart.addTag("kicadTags", "UFBGA-32")
newPart.addTag("kicadAttr", "smd")
newPart.addTag("kicad3DModel", "${KICAD6_3DMODEL_DIR}/Package_BGA.3dshapes/UFBGA-32_4.0x4.0mm_Layout6x6_P0.5mm.wrl")

OOMP.parts.append(newPart)