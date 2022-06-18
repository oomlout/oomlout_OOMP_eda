###### OOMP FILE  ######

import OOMP

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "kicad")
newPart.addTag("oompColor", "kicad-footprints")
newPart.addTag("oompDesc", "Symbol")
newPart.addTag("oompIndex", "UKCA-Logo_30x30mm_SilkScreen")

newPart.addTag("kicadDesc", "UKCA marking")
newPart.addTag("kicadTags", "Logo UKCA marking")
newPart.addTag("kicadAttr", "exclude_from_pos_files exclude_from_bom")

OOMP.parts.append(newPart)