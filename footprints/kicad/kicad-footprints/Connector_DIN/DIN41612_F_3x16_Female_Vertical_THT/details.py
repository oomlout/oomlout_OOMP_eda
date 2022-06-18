###### OOMP FILE  ######

import OOMP

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "kicad")
newPart.addTag("oompColor", "kicad-footprints")
newPart.addTag("oompDesc", "Connector_DIN")
newPart.addTag("oompIndex", "DIN41612_F_3x16_Female_Vertical_THT")

newPart.addTag("kicadDesc", "DIN41612 connector, type F, Vertical, 3 rows 32 pins wide, https://www.erni-x-press.com/de/downloads/kataloge/englische_kataloge/erni-din41612-iec60603-2-e.pdf")
newPart.addTag("kicadTags", "DIN 41612 IEC 60603 F")
newPart.addTag("kicadAttr", "through_hole")
newPart.addTag("kicad3DModel", "${KICAD6_3DMODEL_DIR}/Connector_DIN.3dshapes/DIN41612_F_3x16_Female_Vertical_THT.wrl")

OOMP.parts.append(newPart)