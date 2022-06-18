###### OOMP FILE  ######

import OOMP

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "kicad")
newPart.addTag("oompColor", "kicad-footprints")
newPart.addTag("oompDesc", "Connector")
newPart.addTag("oompIndex", "Tag-Connect_TC2050-IDC-NL_2x05_P1.27mm_Vertical_with_bottom_clip")

newPart.addTag("kicadDesc", "Tag-Connect programming header with bottom courtyard for TC2050-NL Clip board ; https://www.tag-connect.com/wp-content/uploads/bsk-pdf-manager/TC2050-IDC-NL_Datasheet_8.pdf https://www.tag-connect.com/wp-content/uploads/bsk-pdf-manager/TC2050-CLIP_Datasheet_25.pdf")
newPart.addTag("kicadTags", "tag connect programming header pogo pins")
newPart.addTag("kicadAttr", "exclude_from_pos_files exclude_from_bom")

OOMP.parts.append(newPart)