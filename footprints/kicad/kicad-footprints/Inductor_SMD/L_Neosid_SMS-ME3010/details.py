###### OOMP FILE  ######

import OOMP

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "kicad")
newPart.addTag("oompColor", "kicad-footprints")
newPart.addTag("oompDesc", "Inductor_SMD")
newPart.addTag("oompIndex", "L_Neosid_SMS-ME3010")

newPart.addTag("kicadDesc", "Neosid, Inductor, SMS-ME3010, Fixed inductor, SMD, magnetically shielded, https://neosid.de/import-data/product-pdf/neoFestind_SMSME3010.pdf")
newPart.addTag("kicadTags", "Neosid Inductor SMS-ME3010 Fixed inductor SMD magnetically shielded")
newPart.addTag("kicadAttr", "smd")
newPart.addTag("kicad3DModel", "${KICAD6_3DMODEL_DIR}/Inductor_SMD.3dshapes/L_Neosid_SMS-ME3010.wrl")

OOMP.parts.append(newPart)