###### OOMP FILE  ######

import OOMP

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "kicad")
newPart.addTag("oompColor", "kicad-footprints")
newPart.addTag("oompDesc", "Inductor_SMD")
newPart.addTag("oompIndex", "L_TDK_NLV25_2.5x2.0mm")

newPart.addTag("kicadDesc", "TDK NLV25, 2.5x2.0x1.8mm, https://product.tdk.com/info/en/catalog/datasheets/inductor_commercial_standard_nlv25-ef_en.pdf")
newPart.addTag("kicadTags", "tdk nlv25 nlcv25 nlfv25")
newPart.addTag("kicadAttr", "smd")
newPart.addTag("kicad3DModel", "${KICAD6_3DMODEL_DIR}/Inductor_SMD.3dshapes/L_TDK_NLV25_2.5x2.0mm.wrl")

OOMP.parts.append(newPart)