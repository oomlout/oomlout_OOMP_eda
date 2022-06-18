###### OOMP FILE  ######

import OOMP

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "kicad")
newPart.addTag("oompColor", "kicad-footprints")
newPart.addTag("oompDesc", "Package_BGA")
newPart.addTag("oompIndex", "Texas_DSBGA-8_1.43x1.41mm_Layout3x3_P0.5mm")
newPart.addTag("oompName", "kicad-footprints/Package_BGA/Texas_DSBGA-8_1.43x1.41mm_Layout3x3_P0.5mm")

newPart.addTag("kicadDesc", "Texas Instruments, DSBGA, 1.43x1.41mm, 8 bump 3x3 (perimeter) array, NSMD pad definition (http://www.ti.com/lit/ds/symlink/lmc555.pdf, http://www.ti.com/lit/an/snva009ag/snva009ag.pdf)")
newPart.addTag("kicadTags", "Texas Instruments DSBGA BGA YZP R-XBGA-N8")
newPart.addTag("kicadAttr", "smd")
newPart.addTag("kicad3DModel", "${KICAD6_3DMODEL_DIR}/Package_BGA.3dshapes/Texas_DSBGA-8_1.43x1.41mm_Layout3x3_P0.5mm.wrl")

OOMP.parts.append(newPart)