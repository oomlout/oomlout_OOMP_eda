###### OOMP FILE  ######

import OOMP

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "kicad")
newPart.addTag("oompColor", "kicad-footprints")
newPart.addTag("oompDesc", "Package_DFN_QFN")
newPart.addTag("oompIndex", "Texas_QFN-41_10x16mm")

newPart.addTag("kicadDesc", "QFN, 41 Pin (http://www.ti.com/lit/ml/mpqf506/mpqf506.pdf)")
newPart.addTag("kicadTags", "QFN DFN_QFN")
newPart.addTag("kicadAttr", "smd")
newPart.addTag("kicad3DModel", "${KICAD6_3DMODEL_DIR}/Package_DFN_QFN.3dshapes/Texas_QFN-41_10x16mm.wrl")

OOMP.parts.append(newPart)