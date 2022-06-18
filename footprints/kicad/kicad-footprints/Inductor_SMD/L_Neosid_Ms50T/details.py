###### OOMP FILE  ######

import OOMP

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "kicad")
newPart.addTag("oompColor", "kicad-footprints")
newPart.addTag("oompDesc", "Inductor_SMD")
newPart.addTag("oompIndex", "L_Neosid_Ms50T")

newPart.addTag("kicadDesc", "Neosid, Power Inductor, Ms50T, SMD, Fixed inductor,  high temperature, https://neosid.de/import-data/product-pdf/neoFestind_Ms50T.pdf")
newPart.addTag("kicadTags", "Neosid Power Inductor Ms50T SMD Fixed inductor high temperature")
newPart.addTag("kicadAttr", "smd")
newPart.addTag("kicad3DModel", "${KICAD6_3DMODEL_DIR}/Inductor_SMD.3dshapes/L_Neosid_Ms50T.wrl")

OOMP.parts.append(newPart)