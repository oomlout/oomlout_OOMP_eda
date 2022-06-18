###### OOMP FILE  ######

import OOMP

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "kicad")
newPart.addTag("oompColor", "kicad-footprints")
newPart.addTag("oompDesc", "Package_BGA")
newPart.addTag("oompIndex", "Texas_DSBGA-9_1.4715x1.4715mm_Layout3x3_P0.5mm")

newPart.addTag("kicadDesc", "Texas Instruments, DSBGA, 1.4715x1.4715mm, 9 bump 3x3 array, NSMD pad definition (http://www.ti.com/lit/ds/symlink/lm4990.pdf, http://www.ti.com/lit/an/snva009ag/snva009ag.pdf)")
newPart.addTag("kicadTags", "Texas Instruments DSBGA BGA YZR0009")
newPart.addTag("kicadAttr", "smd")
newPart.addTag("kicad3DModel", "${KICAD6_3DMODEL_DIR}/Package_BGA.3dshapes/Texas_DSBGA-9_1.4715x1.4715mm_Layout3x3_P0.5mm.wrl")

OOMP.parts.append(newPart)