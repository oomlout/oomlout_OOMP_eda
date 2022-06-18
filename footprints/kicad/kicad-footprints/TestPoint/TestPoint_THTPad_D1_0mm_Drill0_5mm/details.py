###### OOMP FILE  ######

import OOMP

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "kicad")
newPart.addTag("oompColor", "kicad-footprints")
newPart.addTag("oompDesc", "TestPoint")
newPart.addTag("oompIndex", "TestPoint_THTPad_D1.0mm_Drill0.5mm")

newPart.addTag("kicadDesc", "THT pad as test Point, diameter 1.0mm, hole diameter 0.5mm")
newPart.addTag("kicadTags", "test point THT pad")
newPart.addTag("kicadAttr", "exclude_from_pos_files exclude_from_bom")

OOMP.parts.append(newPart)