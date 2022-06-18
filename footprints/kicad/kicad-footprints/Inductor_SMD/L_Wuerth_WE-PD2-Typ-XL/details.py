###### OOMP FILE  ######

import OOMP

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "kicad")
newPart.addTag("oompColor", "kicad-footprints")
newPart.addTag("oompDesc", "Inductor_SMD")
newPart.addTag("oompIndex", "L_Wuerth_WE-PD2-Typ-XL")

newPart.addTag("kicadDesc", "Power Inductor, Wuerth Elektronik, WE-PD2, SMT, Typ XL, https://katalog.we-online.com/pbs/datasheet/744776012.pdf")
newPart.addTag("kicadTags", "Choke Power Inductor WE-PD2 TypXL Wuerth")
newPart.addTag("kicadAttr", "smd")
newPart.addTag("kicad3DModel", "${KICAD6_3DMODEL_DIR}/Inductor_SMD.3dshapes/L_Wuerth_WE-PD2-Typ-XL.wrl")

OOMP.parts.append(newPart)