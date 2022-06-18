###### OOMP FILE  ######

import OOMP

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "kicad")
newPart.addTag("oompColor", "kicad-footprints")
newPart.addTag("oompDesc", "TestPoint")
newPart.addTag("oompIndex", "TestPoint_THTPad_D3.0mm_Drill1.5mm")
newPart.addTag("oompName", "kicad-footprints/TestPoint/TestPoint_THTPad_D3.0mm_Drill1.5mm")

newPart.addTag("kicadDesc", "THT pad as test Point, diameter 3.0mm, hole diameter 1.5mm")
newPart.addTag("kicadTags", "test point THT pad")
newPart.addTag("kicadAttr", "exclude_from_pos_files exclude_from_bom")

OOMP.parts.append(newPart)