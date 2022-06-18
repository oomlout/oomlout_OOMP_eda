###### OOMP FILE  ######

import OOMP

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "kicad")
newPart.addTag("oompColor", "kicad-footprints")
newPart.addTag("oompDesc", "Connector_RJ")
newPart.addTag("oompIndex", "RJ45_Wuerth_74980111211_Horizontal")

newPart.addTag("kicadDesc", "RJ45 LAN Transformer 10/100BaseT (https://katalog.we-online.de/pbs/datasheet/74980111211.pdf)")
newPart.addTag("kicadTags", "lan magnetics transformer")
newPart.addTag("kicadAttr", "smd")
newPart.addTag("kicad3DModel", "${KICAD6_3DMODEL_DIR}/Connector_RJ.3dshapes/RJ45_Wuerth_74980111211_Horizontal.wrl")

OOMP.parts.append(newPart)