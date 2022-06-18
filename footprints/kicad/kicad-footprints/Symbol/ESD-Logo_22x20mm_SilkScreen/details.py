###### OOMP FILE  ######

import OOMP

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "kicad")
newPart.addTag("oompColor", "kicad-footprints")
newPart.addTag("oompDesc", "Symbol")
newPart.addTag("oompIndex", "ESD-Logo_22x20mm_SilkScreen")

newPart.addTag("kicadDesc", "Electrostatic discharge Logo")
newPart.addTag("kicadTags", "Logo ESD")
newPart.addTag("kicadAttr", "exclude_from_pos_files exclude_from_bom")

OOMP.parts.append(newPart)