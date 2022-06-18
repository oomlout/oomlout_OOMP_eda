###### OOMP FILE  ######

import OOMP

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "kicad")
newPart.addTag("oompColor", "kicad-footprints")
newPart.addTag("oompDesc", "RF_Antenna")
newPart.addTag("oompIndex", "Texas_SWRA117D_2.4GHz_Left")

newPart.addTag("kicadDesc", "http://www.ti.com/lit/an/swra117d/swra117d.pdf")
newPart.addTag("kicadTags", "PCB antenna")
newPart.addTag("kicadAttr", "exclude_from_pos_files exclude_from_bom")

OOMP.parts.append(newPart)