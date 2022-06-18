###### OOMP FILE  ######

import OOMP

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "kicad")
newPart.addTag("oompColor", "kicad-footprints")
newPart.addTag("oompDesc", "Jumper")
newPart.addTag("oompIndex", "SolderJumper-3_P1.3mm_Open_Pad1.0x1.5mm_NumberLabels")

newPart.addTag("kicadDesc", "SMD Solder Jumper, 1x1.5mm Pads, 0.3mm gap, open, labeled with numbers")
newPart.addTag("kicadTags", "solder jumper open")
newPart.addTag("kicadAttr", "exclude_from_pos_files exclude_from_bom")

OOMP.parts.append(newPart)