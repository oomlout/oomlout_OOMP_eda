###### OOMP FILE  ######

import OOMP

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "kicad")
newPart.addTag("oompColor", "kicad-footprints")
newPart.addTag("oompDesc", "Connector_RJ")
newPart.addTag("oompIndex", "RJ45_Wuerth_7499151120_Horizontal")

newPart.addTag("kicadDesc", "Wuerth 7499151120, LAN-Transformer WE-RJ45LAN 10/100/1000 BaseT, Dual Ethernet Jack (http://katalog.we-online.de/pbs/datasheet/7499151120.pdf)")
newPart.addTag("kicadTags", "ethernet lan connector")
newPart.addTag("kicadAttr", "through_hole")
newPart.addTag("kicad3DModel", "${KICAD6_3DMODEL_DIR}/Connector_RJ.3dshapes/RJ45_Wuerth_7499151120_Horizontal.wrl")

OOMP.parts.append(newPart)