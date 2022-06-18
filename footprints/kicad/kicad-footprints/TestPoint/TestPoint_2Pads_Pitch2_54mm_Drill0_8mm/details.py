###### OOMP FILE  ######

import OOMP

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "kicad")
newPart.addTag("oompColor", "kicad-footprints")
newPart.addTag("oompDesc", "TestPoint")
newPart.addTag("oompIndex", "TestPoint_2Pads_Pitch2.54mm_Drill0.8mm")

newPart.addTag("kicadDesc", "Test point with 2 pins, pitch 2.54mm, drill diameter 0.8mm")
newPart.addTag("kicadTags", "CONN DEV")
newPart.addTag("kicadAttr", "exclude_from_pos_files exclude_from_bom")

OOMP.parts.append(newPart)