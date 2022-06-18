###### OOMP FILE  ######

import OOMP

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "kicad")
newPart.addTag("oompColor", "kicad-footprints")
newPart.addTag("oompDesc", "Jumper")
newPart.addTag("oompIndex", "SolderJumper-2_P1.3mm_Bridged2Bar_Pad1.0x1.5mm")

newPart.addTag("kicadDesc", "SMD Solder Jumper, 1x1.5mm Pads, 0.3mm gap, bridged with 2 copper strips")
newPart.addTag("kicadTags", "net tie solder jumper bridged")
newPart.addTag("kicadAttr", "exclude_from_pos_files exclude_from_bom")

OOMP.parts.append(newPart)