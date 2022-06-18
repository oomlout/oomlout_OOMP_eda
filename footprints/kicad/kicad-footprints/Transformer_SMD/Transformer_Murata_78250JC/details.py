###### OOMP FILE  ######

import OOMP

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "kicad")
newPart.addTag("oompColor", "kicad-footprints")
newPart.addTag("oompDesc", "Transformer_SMD")
newPart.addTag("oompIndex", "Transformer_Murata_78250JC")

newPart.addTag("kicadDesc", "Murata 78250JC https://www.murata-ps.com/datasheet?/data/magnetics/kmp_78250j.pdf")
newPart.addTag("kicadTags", "Murata transformer")
newPart.addTag("kicadAttr", "smd")
newPart.addTag("kicad3DModel", "${KICAD6_3DMODEL_DIR}/Transformer_SMD.3dshapes/Transformer_Murata_78250JC.wrl")

OOMP.parts.append(newPart)