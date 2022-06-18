###### OOMP FILE  ######

import OOMP

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "kicad")
newPart.addTag("oompColor", "kicad-footprints")
newPart.addTag("oompDesc", "Package_BGA")
newPart.addTag("oompIndex", "Texas_DSBGA-28_1.9x3.0mm_Layout4x7_P0.4mm")

newPart.addTag("kicadDesc", "Texas Instruments, DSBGA, 3.0x1.9x0.625mm, 28 ball 7x4 area grid, NSMD pad definition (http://www.ti.com/lit/ds/symlink/bq51050b.pdf, http://www.ti.com/lit/an/snva009ag/snva009ag.pdf)")
newPart.addTag("kicadTags", "BGA 28 0.4")
newPart.addTag("kicadAttr", "smd")
newPart.addTag("kicad3DModel", "${KICAD6_3DMODEL_DIR}/Package_BGA.3dshapes/Texas_DSBGA-28_1.9x3.0mm_Layout4x7_P0.4mm.wrl")

OOMP.parts.append(newPart)