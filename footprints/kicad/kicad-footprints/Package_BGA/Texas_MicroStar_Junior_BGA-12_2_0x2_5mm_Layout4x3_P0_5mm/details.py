###### OOMP FILE  ######

import OOMP

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "kicad")
newPart.addTag("oompColor", "kicad-footprints")
newPart.addTag("oompDesc", "Package_BGA")
newPart.addTag("oompIndex", "Texas_MicroStar_Junior_BGA-12_2.0x2.5mm_Layout4x3_P0.5mm")

newPart.addTag("kicadDesc", "Texas Instruments, BGA Microstar Junior, 2x2.5mm, 12 bump 4x3 grid, NSMD pad definition (http://www.ti.com/lit/ds/symlink/txb0104.pdf, http://www.ti.com/lit/wp/ssyz015b/ssyz015b.pdf)")
newPart.addTag("kicadTags", "Texas_Junior_BGA-12")
newPart.addTag("kicadAttr", "smd")
newPart.addTag("kicad3DModel", "${KICAD6_3DMODEL_DIR}/Package_BGA.3dshapes/Texas_MicroStar_Junior_BGA-12_2.0x2.5mm_Layout4x3_P0.5mm.wrl")

OOMP.parts.append(newPart)