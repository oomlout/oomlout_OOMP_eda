###### OOMP FILE  ######

import OOMP

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "kicad")
newPart.addTag("oompColor", "kicad-footprints")
newPart.addTag("oompDesc", "Display")
newPart.addTag("oompIndex", "WC1602A")

newPart.addTag("kicadDesc", "LCD 16x2 http://www.wincomlcd.com/pdf/WC1602A-SFYLYHTC06.pdf")
newPart.addTag("kicadTags", "LCD 16x2 Alphanumeric 16pin")
newPart.addTag("kicadAttr", "through_hole")
newPart.addTag("kicad3DModel", "${KICAD6_3DMODEL_DIR}/Display.3dshapes/WC1602A.wrl")

OOMP.parts.append(newPart)