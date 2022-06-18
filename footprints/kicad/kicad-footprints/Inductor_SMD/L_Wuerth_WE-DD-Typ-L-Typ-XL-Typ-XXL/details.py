###### OOMP FILE  ######

import OOMP

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "kicad")
newPart.addTag("oompColor", "kicad-footprints")
newPart.addTag("oompDesc", "Inductor_SMD")
newPart.addTag("oompIndex", "L_Wuerth_WE-DD-Typ-L-Typ-XL-Typ-XXL")

newPart.addTag("kicadDesc", "Shielded Coupled Inductor, Wuerth Elektronik, WE-DD, SMD, Typ L, Typ XL, Typ XXL, https://katalog.we-online.com/pbs/datasheet/744874001.pdf")
newPart.addTag("kicadTags", "Choke Coupled Double Inductor SMD Wuerth WE-DD TypL TypXL TypXXL")
newPart.addTag("kicadAttr", "smd")
newPart.addTag("kicad3DModel", "${KICAD6_3DMODEL_DIR}/Inductor_SMD.3dshapes/L_Wuerth_WE-DD-Typ-L-Typ-XL-Typ-XXL.wrl")

OOMP.parts.append(newPart)