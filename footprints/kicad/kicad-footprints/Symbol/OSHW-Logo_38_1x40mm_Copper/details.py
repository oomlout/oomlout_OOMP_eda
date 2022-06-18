###### OOMP FILE  ######

import OOMP

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "kicad")
newPart.addTag("oompColor", "kicad-footprints")
newPart.addTag("oompDesc", "Symbol")
newPart.addTag("oompIndex", "OSHW-Logo_38.1x40mm_Copper")

newPart.addTag("kicadDesc", "Open Source Hardware Logo")
newPart.addTag("kicadTags", "Logo OSHW")
newPart.addTag("kicadAttr", "exclude_from_pos_files exclude_from_bom")

OOMP.parts.append(newPart)