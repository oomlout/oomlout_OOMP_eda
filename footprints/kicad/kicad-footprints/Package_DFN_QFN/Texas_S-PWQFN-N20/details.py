###### OOMP FILE  ######

import OOMP

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "kicad")
newPart.addTag("oompColor", "kicad-footprints")
newPart.addTag("oompDesc", "Package_DFN_QFN")
newPart.addTag("oompIndex", "Texas_S-PWQFN-N20")

newPart.addTag("kicadDesc", "20-Pin Plastic Quad Flatpack No-Lead Package, Body 3.0x3.0x0.8mm, Texas Instruments (http://www.ti.com/lit/ds/symlink/tps22993.pdf)")
newPart.addTag("kicadTags", "QFN 0.4")
newPart.addTag("kicadAttr", "smd")
newPart.addTag("kicad3DModel", "${KICAD6_3DMODEL_DIR}/Package_DFN_QFN.3dshapes/Texas_S-PWQFN-N20.wrl")

OOMP.parts.append(newPart)