###### OOMP FILE  ######

import OOMP

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "kicad")
newPart.addTag("oompColor", "kicad-footprints")
newPart.addTag("oompDesc", "Diode_SMD")
newPart.addTag("oompIndex", "Diode_Bridge_Bourns_CD-DF4xxS")

newPart.addTag("kicadDesc", "8.1x10.5mm, 4A, single phase bridge rectifier, https://www.bourns.com/docs/Product-Datasheets/CD-DF4xxSL.pdf")
newPart.addTag("kicadTags", "Surface Mount Bridge Rectifier Diode")
newPart.addTag("kicadAttr", "smd")
newPart.addTag("kicad3DModel", "${KICAD6_3DMODEL_DIR}/Diode_SMD.3dshapes/Diode_Bridge_Bourns_CD-DF4xxS.wrl")

OOMP.parts.append(newPart)