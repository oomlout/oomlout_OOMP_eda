###### OOMP FILE  ######

import OOMP

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "kicad")
newPart.addTag("oompColor", "kicad-footprints")
newPart.addTag("oompDesc", "Package_BGA")
newPart.addTag("oompIndex", "Texas_MicroStar_Junior_BGA-80_5.0x5.0mm_Layout9x9_P0.5mm")

newPart.addTag("kicadDesc", "Texas Instruments, BGA Microstar Junior, 5x5mm, 80 ball 9x9 grid, NSMD pad definition (http://www.ti.com/lit/ds/symlink/tlv320aic23b.pdf, http://www.ti.com/lit/wp/ssyz015b/ssyz015b.pdf)")
newPart.addTag("kicadTags", "Texas_Junior_BGA-80")
newPart.addTag("kicadAttr", "smd")
newPart.addTag("kicad3DModel", "${KICAD6_3DMODEL_DIR}/Package_BGA.3dshapes/Texas_MicroStar_Junior_BGA-80_5.0x5.0mm_Layout9x9_P0.5mm.wrl")

OOMP.parts.append(newPart)