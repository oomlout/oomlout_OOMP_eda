###### OOMP FILE  ######

import OOMP

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "kicad")
newPart.addTag("oompColor", "kicad-footprints")
newPart.addTag("oompDesc", "Package_DFN_QFN")
newPart.addTag("oompIndex", "Texas_MOF0009A")

newPart.addTag("kicadDesc", "Texas Instruments, QFM MOF0009A, 6x8x2mm (http://www.ti.com/lit/ml/mpsi063a/mpsi063a.pdf)")
newPart.addTag("kicadTags", "ti qfm mof0009a")
newPart.addTag("kicadAttr", "smd")
newPart.addTag("kicad3DModel", "${KICAD6_3DMODEL_DIR}/Package_DFN_QFN.3dshapes/Texas_MOF0009A.wrl")

OOMP.parts.append(newPart)