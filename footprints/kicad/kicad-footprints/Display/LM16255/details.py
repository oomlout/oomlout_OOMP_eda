###### OOMP FILE  ######

import OOMP

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "kicad")
newPart.addTag("oompColor", "kicad-footprints")
newPart.addTag("oompDesc", "Display")
newPart.addTag("oompIndex", "LM16255")

newPart.addTag("kicadDesc", "LCD LM16255 16x2 character http://www.datasheetlib.com/datasheet/259542/lm16255_sharp-electronics.html")
newPart.addTag("kicadTags", "LCD 12x2")
newPart.addTag("kicadAttr", "through_hole")
newPart.addTag("kicad3DModel", "${KICAD6_3DMODEL_DIR}/Display.3dshapes/LM16255.wrl")

OOMP.parts.append(newPart)