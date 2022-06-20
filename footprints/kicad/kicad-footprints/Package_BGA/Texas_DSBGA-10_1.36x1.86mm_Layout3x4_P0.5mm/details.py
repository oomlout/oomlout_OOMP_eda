###### OOMP FILE  ######

import OOMP

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "kicad")
newPart.addTag("oompColor", "kicad-footprints")
newPart.addTag("oompDesc", "Package_BGA")
newPart.addTag("oompIndex", "Texas_DSBGA-10_1.36x1.86mm_Layout3x4_P0.5mm")
newPart.addTag("oompName", "kicad-footprints/Package_BGA/Texas_DSBGA-10_1.36x1.86mm_Layout3x4_P0.5mm")

newPart.addTag("kicadDesc", "Texas Instruments, DSBGA, 1.36x1.86mm, 10 bump 3x4 (perimeter) array, NSMD pad definition (http://www.ti.com/lit/ds/symlink/txs0104e.pdf, http://www.ti.com/lit/an/snva009ag/snva009ag.pdf)")
newPart.addTag("kicadTags", "Texas Instruments DSBGA BGA")
newPart.addTag("kicadAttr", "smd")
newPart.addTag("kicad3DModel", "${KICAD6_3DMODEL_DIR}/Package_BGA.3dshapes/Texas_DSBGA-10_1.36x1.86mm_Layout3x4_P0.5mm.wrl")

OOMP.parts.append(newPart)