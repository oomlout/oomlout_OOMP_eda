###### OOMP FILE  ######

import OOMP

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "kicad")
newPart.addTag("oompColor", "kicad-footprints")
newPart.addTag("oompDesc", "Package_BGA")
newPart.addTag("oompIndex", "Texas_DSBGA-49_3.33x3.488mm_Layout7x7_P0.4mm")

newPart.addTag("kicadDesc", "Texas Instruments, DSBGA, 3.33x3.488x0.625mm, 49 ball 7x7 area grid, NSMD pad definition (http://www.ti.com/lit/ds/symlink/msp430f2234.pdf, http://www.ti.com/lit/an/snva009ag/snva009ag.pdf)")
newPart.addTag("kicadTags", "texas dsbga 49")
newPart.addTag("kicadAttr", "smd")
newPart.addTag("kicad3DModel", "${KICAD6_3DMODEL_DIR}/Package_BGA.3dshapes/Texas_DSBGA-49_3.33x3.488mm_Layout7x7_P0.4mm.wrl")

OOMP.parts.append(newPart)