###### OOMP FILE  ######

import OOMP

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "kicad")
newPart.addTag("oompColor", "kicad-footprints")
newPart.addTag("oompDesc", "Package_BGA")
newPart.addTag("oompIndex", "Texas_DSBGA-5_0.822x1.116mm_Layout2x1x2_P0.4mm")

newPart.addTag("kicadDesc", "Texas Instruments, DSBGA, 0.822x1.116mm, 5 bump 2x1x2 array, NSMD pad definition (http://www.ti.com/lit/ds/symlink/opa330.pdf, http://www.ti.com/lit/an/snva009ag/snva009ag.pdf)")
newPart.addTag("kicadTags", "Texas Instruments DSBGA BGA YFF S-XBGA-N5")
newPart.addTag("kicadAttr", "smd")
newPart.addTag("kicad3DModel", "${KICAD6_3DMODEL_DIR}/Package_BGA.3dshapes/Texas_DSBGA-5_0.822x1.116mm_Layout2x1x2_P0.4mm.wrl")

OOMP.parts.append(newPart)