###### OOMP FILE  ######

import OOMP

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "kicad")
newPart.addTag("oompColor", "kicad-footprints")
newPart.addTag("oompDesc", "Relay_SMD")
newPart.addTag("oompIndex", "Relay_Fujitsu_FTR-B3S")

newPart.addTag("kicadDesc", "https://www.fujitsu.com/downloads/MICRO/fcai/relays/ftr-b3.pdf")
newPart.addTag("kicadTags", "Fujitsh FTR B3S B3SA Relay J JLeg")
newPart.addTag("kicadAttr", "smd")
newPart.addTag("kicad3DModel", "${KICAD6_3DMODEL_DIR}/Relay_SMD.3dshapes/Relay_Fujitsu_FTR-B3S.wrl")

OOMP.parts.append(newPart)