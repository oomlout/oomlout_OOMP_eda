###### OOMP FILE  ######

import OOMP

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "kicad")
newPart.addTag("oompColor", "kicad-footprints")
newPart.addTag("oompDesc", "Inductor_SMD")
newPart.addTag("oompIndex", "L_Wuerth_HCF-2013")

newPart.addTag("kicadDesc", "7443630070, http://katalog.we-online.de/pbs/datasheet/7443630070.pdf")
newPart.addTag("kicadTags", "inductor shielded wuerth hcf")
newPart.addTag("kicadAttr", "smd")
newPart.addTag("kicad3DModel", "${KICAD6_3DMODEL_DIR}/Inductor_SMD.3dshapes/L_Wuerth_HCF-2013.wrl")

OOMP.parts.append(newPart)