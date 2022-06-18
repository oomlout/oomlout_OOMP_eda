###### OOMP FILE  ######

import OOMP

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "kicad")
newPart.addTag("oompColor", "kicad-footprints")
newPart.addTag("oompDesc", "Jumper")
newPart.addTag("oompIndex", "SolderJumper-3_P2.0mm_Open_TrianglePad1.0x1.5mm")

newPart.addTag("kicadDesc", "SMD Solder Jumper, 1x1.5mm Triangular Pads, 0.3mm gap, open")
newPart.addTag("kicadTags", "solder jumper open")
newPart.addTag("kicadAttr", "exclude_from_pos_files exclude_from_bom")

OOMP.parts.append(newPart)