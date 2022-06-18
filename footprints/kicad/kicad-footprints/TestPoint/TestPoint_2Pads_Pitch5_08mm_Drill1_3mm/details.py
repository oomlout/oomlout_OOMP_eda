###### OOMP FILE  ######

import OOMP

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "kicad")
newPart.addTag("oompColor", "kicad-footprints")
newPart.addTag("oompDesc", "TestPoint")
newPart.addTag("oompIndex", "TestPoint_2Pads_Pitch5.08mm_Drill1.3mm")

newPart.addTag("kicadDesc", "Test point with 2 pads, pitch 5.08mm, hole diameter 1.3mm, wire diameter 1.0mm")
newPart.addTag("kicadTags", "CONN DEV")
newPart.addTag("kicadAttr", "exclude_from_pos_files exclude_from_bom")

OOMP.parts.append(newPart)