###### OOMP FILE  ######

import OOMP

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "kicad")
newPart.addTag("oompColor", "kicad-footprints")
newPart.addTag("oompDesc", "Inductor_SMD")
newPart.addTag("oompIndex", "L_Neosid_SMs50")

newPart.addTag("kicadDesc", "Neosid, Inductor, SMs50, Fixed inductor, SMD, magneticaly shielded, https://neosid.de/import-data/product-pdf/neoFestind_ma_SMs50.pdf")
newPart.addTag("kicadTags", "Neosid Inductor SMs50 Fixed inductor SMD magneticaly shielded")
newPart.addTag("kicadAttr", "smd")
newPart.addTag("kicad3DModel", "${KICAD6_3DMODEL_DIR}/Inductor_SMD.3dshapes/L_Neosid_SMs50.wrl")

OOMP.parts.append(newPart)