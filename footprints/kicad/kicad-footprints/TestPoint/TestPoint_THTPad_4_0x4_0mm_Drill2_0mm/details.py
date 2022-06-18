###### OOMP FILE  ######

import OOMP

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "kicad")
newPart.addTag("oompColor", "kicad-footprints")
newPart.addTag("oompDesc", "TestPoint")
newPart.addTag("oompIndex", "TestPoint_THTPad_4.0x4.0mm_Drill2.0mm")

newPart.addTag("kicadDesc", "THT rectangular pad as test Point, square 4.0mm  side length, hole diameter 2.0mm")
newPart.addTag("kicadTags", "test point THT pad rectangle square")
newPart.addTag("kicadAttr", "exclude_from_pos_files exclude_from_bom")

OOMP.parts.append(newPart)