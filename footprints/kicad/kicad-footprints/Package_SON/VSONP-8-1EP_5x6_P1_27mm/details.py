###### OOMP FILE  ######

import OOMP

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "kicad")
newPart.addTag("oompColor", "kicad-footprints")
newPart.addTag("oompDesc", "Package_SON")
newPart.addTag("oompIndex", "VSONP-8-1EP_5x6_P1.27mm")

newPart.addTag("kicadDesc", "SON, 8-Leads, Body 5x6x1mm, Pitch 1.27mm; (see Texas Instruments CSD18531Q5A http://www.ti.com/lit/ds/symlink/csd18531q5a.pdf)")
newPart.addTag("kicadTags", "VSONP 1.27")
newPart.addTag("kicadAttr", "smd")
newPart.addTag("kicad3DModel", "${KICAD6_3DMODEL_DIR}/Package_SON.3dshapes/VSONP-8-1EP_5x6_P1.27mm.wrl")

OOMP.parts.append(newPart)