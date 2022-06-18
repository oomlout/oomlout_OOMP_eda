###### OOMP FILE  ######

import OOMP

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "kicad")
newPart.addTag("oompColor", "kicad-footprints")
newPart.addTag("oompDesc", "Package_BGA")
newPart.addTag("oompIndex", "Texas_DSBGA-6_0.9x1.4mm_Layout2x3_P0.5mm")
newPart.addTag("oompName", "kicad-footprints/Package_BGA/Texas_DSBGA-6_0.9x1.4mm_Layout2x3_P0.5mm")

newPart.addTag("kicadDesc", "Texas Instruments, DSBGA, 0.9x1.4mm, 6 bump 2x3 (perimeter) array, NSMD pad definition (http://www.ti.com/lit/ds/symlink/ts5a3159a.pdf)")
newPart.addTag("kicadTags", "Texas Instruments DSBGA BGA YZP R-XBGA-N6")
newPart.addTag("kicadAttr", "smd")
newPart.addTag("kicad3DModel", "${KICAD6_3DMODEL_DIR}/Package_BGA.3dshapes/Texas_DSBGA-6_0.9x1.4mm_Layout2x3_P0.5mm.wrl")

OOMP.parts.append(newPart)