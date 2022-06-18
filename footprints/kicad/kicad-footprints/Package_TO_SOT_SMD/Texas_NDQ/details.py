###### OOMP FILE  ######

import OOMP

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "kicad")
newPart.addTag("oompColor", "kicad-footprints")
newPart.addTag("oompDesc", "Package_TO_SOT_SMD")
newPart.addTag("oompIndex", "Texas_NDQ")

newPart.addTag("kicadDesc", "Texas Instruments, NDQ, 5 pin (https://www.ti.com/lit/ml/mmsf022/mmsf022.pdf)")
newPart.addTag("kicadTags", "ti pfm dap")
newPart.addTag("kicadAttr", "smd")
newPart.addTag("kicad3DModel", "${KICAD6_3DMODEL_DIR}/Package_TO_SOT_SMD.3dshapes/Texas_NDQ.wrl")

OOMP.parts.append(newPart)