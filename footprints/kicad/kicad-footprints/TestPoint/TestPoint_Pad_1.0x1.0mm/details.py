###### OOMP FILE  ######

import OOMP

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "kicad")
newPart.addTag("oompColor", "kicad-footprints")
newPart.addTag("oompDesc", "TestPoint")
newPart.addTag("oompIndex", "TestPoint_Pad_1.0x1.0mm")
newPart.addTag("oompName", "kicad-footprints/TestPoint/TestPoint_Pad_1.0x1.0mm")

newPart.addTag("kicadDesc", "SMD rectangular pad as test Point, square 1.0mm side length")
newPart.addTag("kicadTags", "test point SMD pad rectangle square")
newPart.addTag("kicadAttr", "exclude_from_pos_files exclude_from_bom")

OOMP.parts.append(newPart)