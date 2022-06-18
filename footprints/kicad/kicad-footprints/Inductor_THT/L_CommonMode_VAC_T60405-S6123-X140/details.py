###### OOMP FILE  ######

import OOMP

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "kicad")
newPart.addTag("oompColor", "kicad-footprints")
newPart.addTag("oompDesc", "Inductor_THT")
newPart.addTag("oompIndex", "L_CommonMode_VAC_T60405-S6123-X140")

newPart.addTag("kicadDesc", "3 Phase, CM Choke, https://vacuumschmelze.com/03_Documents/Datasheets%20-%20Drawings/Commom-Mode-Chokes/6123-X140.pdf")
newPart.addTag("kicadTags", "common mode filter")
newPart.addTag("kicadAttr", "through_hole")
newPart.addTag("kicad3DModel", "${KICAD6_3DMODEL_DIR}/Inductor_THT.3dshapes/L_CommonMode_VAC_T60405-S6123-X140.wrl")

OOMP.parts.append(newPart)