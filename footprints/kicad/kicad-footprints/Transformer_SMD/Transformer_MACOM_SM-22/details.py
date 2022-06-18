###### OOMP FILE  ######

import OOMP

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "kicad")
newPart.addTag("oompColor", "kicad-footprints")
newPart.addTag("oompDesc", "Transformer_SMD")
newPart.addTag("oompIndex", "Transformer_MACOM_SM-22")

newPart.addTag("kicadDesc", "https://cdn.macom.com/datasheets/ETC1-1-13.pdf")
newPart.addTag("kicadTags", "RF Transformer")
newPart.addTag("kicadAttr", "smd")
newPart.addTag("kicad3DModel", "${KICAD6_3DMODEL_DIR}/Transformer_SMD.3dshapes/Transformer_MACOM_SM-22.wrl")

OOMP.parts.append(newPart)