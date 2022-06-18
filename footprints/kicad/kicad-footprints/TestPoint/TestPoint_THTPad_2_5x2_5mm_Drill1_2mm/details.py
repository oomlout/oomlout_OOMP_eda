###### OOMP FILE  ######

import OOMP

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "kicad")
newPart.addTag("oompColor", "kicad-footprints")
newPart.addTag("oompDesc", "TestPoint")
newPart.addTag("oompIndex", "TestPoint_THTPad_2.5x2.5mm_Drill1.2mm")
newPart.addTag("oompName", "kicad-footprints/TestPoint/TestPoint_THTPad_2.5x2.5mm_Drill1.2mm")

newPart.addTag("kicadDesc", "THT rectangular pad as test Point, square 2.5mm side length, hole diameter 1.2mm")
newPart.addTag("kicadTags", "test point THT pad rectangle square")
newPart.addTag("kicadAttr", "exclude_from_pos_files exclude_from_bom")

OOMP.parts.append(newPart)