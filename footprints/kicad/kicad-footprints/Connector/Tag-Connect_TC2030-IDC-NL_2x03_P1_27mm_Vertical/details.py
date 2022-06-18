###### OOMP FILE  ######

import OOMP

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "kicad")
newPart.addTag("oompColor", "kicad-footprints")
newPart.addTag("oompDesc", "Connector")
newPart.addTag("oompIndex", "Tag-Connect_TC2030-IDC-NL_2x03_P1.27mm_Vertical")

newPart.addTag("kicadDesc", "Tag-Connect programming header; http://www.tag-connect.com/Materials/TC2030-IDC-NL.pdf")
newPart.addTag("kicadTags", "tag connect programming header pogo pins")
newPart.addTag("kicadAttr", "exclude_from_pos_files exclude_from_bom")

OOMP.parts.append(newPart)