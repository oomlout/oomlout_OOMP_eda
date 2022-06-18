###### OOMP FILE  ######

import OOMP

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "kicad")
newPart.addTag("oompColor", "kicad-footprints")
newPart.addTag("oompDesc", "Inductor_SMD")
newPart.addTag("oompIndex", "L_Neosid_SM-NE127_HandSoldering")

newPart.addTag("kicadDesc", "Neosid, Inductor, SM-NE127, Fixed inductor, SMD, https://neosid.de/import-data/product-pdf/neoFestind_SMNE127.pdf")
newPart.addTag("kicadTags", "Neosid Inductor SM-NE127 Fixed inductor SMD")
newPart.addTag("kicadAttr", "smd")
newPart.addTag("kicad3DModel", "${KICAD6_3DMODEL_DIR}/Inductor_SMD.3dshapes/L_Neosid_SM-NE127.wrl")

OOMP.parts.append(newPart)