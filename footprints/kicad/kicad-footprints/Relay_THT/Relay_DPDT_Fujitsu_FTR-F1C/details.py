###### OOMP FILE  ######

import OOMP

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "kicad")
newPart.addTag("oompColor", "kicad-footprints")
newPart.addTag("oompDesc", "Relay_THT")
newPart.addTag("oompIndex", "Relay_DPDT_Fujitsu_FTR-F1C")

newPart.addTag("kicadDesc", "https://www.fujitsu.com/downloads/MICRO/fcai/relays/ftr-f1.pdf")
newPart.addTag("kicadTags", "relay dpdt fujitsu tht")
newPart.addTag("kicadAttr", "through_hole")
newPart.addTag("kicad3DModel", "${KICAD6_3DMODEL_DIR}/Relay_THT.3dshapes/Relay_DPDT_Fujitsu_FTR-F1C.wrl")

OOMP.parts.append(newPart)