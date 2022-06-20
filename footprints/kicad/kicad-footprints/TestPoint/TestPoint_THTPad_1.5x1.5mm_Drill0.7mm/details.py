###### OOMP FILE  ######

import OOMP

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "kicad")
newPart.addTag("oompColor", "kicad-footprints")
newPart.addTag("oompDesc", "TestPoint")
newPart.addTag("oompIndex", "TestPoint_THTPad_1.5x1.5mm_Drill0.7mm")
newPart.addTag("oompName", "kicad-footprints/TestPoint/TestPoint_THTPad_1.5x1.5mm_Drill0.7mm")

newPart.addTag("kicadDesc", "THT rectangular pad as test Point, square 1.5mm side length, hole diameter 0.7mm")
newPart.addTag("kicadTags", "test point THT pad rectangle square")
newPart.addTag("kicadAttr", "exclude_from_pos_files exclude_from_bom")

OOMP.parts.append(newPart)