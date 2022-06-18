###### OOMP FILE  ######

import OOMP

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "kicad")
newPart.addTag("oompColor", "kicad-footprints")
newPart.addTag("oompDesc", "Package_SON")
newPart.addTag("oompIndex", "WSON-6_1.5x1.5mm_P0.5mm")

newPart.addTag("kicadDesc", "WSON6, http://www.ti.com/lit/ds/symlink/tlv702.pdf")
newPart.addTag("kicadTags", "WSON6_1.5x1.5mm_P0.5mm")
newPart.addTag("kicadAttr", "smd")
newPart.addTag("kicad3DModel", "${KICAD6_3DMODEL_DIR}/Package_SON.3dshapes/WSON-6_1.5x1.5mm_P0.5mm.wrl")

OOMP.parts.append(newPart)