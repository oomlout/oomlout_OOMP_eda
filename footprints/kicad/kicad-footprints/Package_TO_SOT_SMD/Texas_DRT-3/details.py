###### OOMP FILE  ######

import OOMP

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "kicad")
newPart.addTag("oompColor", "kicad-footprints")
newPart.addTag("oompDesc", "Package_TO_SOT_SMD")
newPart.addTag("oompIndex", "Texas_DRT-3")

newPart.addTag("kicadDesc", "Texas Instrument DRT-3 1x0.8mm Pitch 0.7mm http://www.ti.com/lit/ds/symlink/tpd2eusb30.pdf")
newPart.addTag("kicadTags", "DRT-3 1x0.8mm Pitch 0.7mm")
newPart.addTag("kicadAttr", "smd")
newPart.addTag("kicad3DModel", "${KICAD6_3DMODEL_DIR}/Package_TO_SOT_SMD.3dshapes/Texas_DRT-3.wrl")

OOMP.parts.append(newPart)