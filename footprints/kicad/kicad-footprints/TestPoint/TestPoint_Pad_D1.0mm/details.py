###### OOMP FILE  ######

import OOMP

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "kicad")
newPart.addTag("oompColor", "kicad-footprints")
newPart.addTag("oompDesc", "TestPoint")
newPart.addTag("oompIndex", "TestPoint_Pad_D1.0mm")
newPart.addTag("oompName", "kicad-footprints/TestPoint/TestPoint_Pad_D1.0mm")

newPart.addTag("kicadDesc", "SMD pad as test Point, diameter 1.0mm")
newPart.addTag("kicadTags", "test point SMD pad")
newPart.addTag("kicadAttr", "exclude_from_pos_files exclude_from_bom")

OOMP.parts.append(newPart)