###### OOMP FILE  ######

import OOMP

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "kicad")
newPart.addTag("oompColor", "kicad-footprints")
newPart.addTag("oompDesc", "Package_DFN_QFN")
newPart.addTag("oompIndex", "Texas_VQFN-RHL-20")

newPart.addTag("kicadDesc", "http://www.ti.com/lit/ds/symlink/bq51050b.pdf")
newPart.addTag("kicadTags", "RHL0020A")
newPart.addTag("kicadAttr", "smd")
newPart.addTag("kicad3DModel", "${KICAD6_3DMODEL_DIR}/Package_DFN_QFN.3dshapes/Texas_VQFN-RHL-20_ThermalVias.wrl")

OOMP.parts.append(newPart)