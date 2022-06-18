###### OOMP FILE  ######

import OOMP

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "kicad")
newPart.addTag("oompColor", "kicad-footprints")
newPart.addTag("oompDesc", "Symbol")
newPart.addTag("oompIndex", "FCC-Logo_7.3x6mm_SilkScreen")

newPart.addTag("kicadDesc", "FCC marking")
newPart.addTag("kicadTags", "Logo FCC certification")
newPart.addTag("kicadAttr", "exclude_from_pos_files exclude_from_bom")

OOMP.parts.append(newPart)