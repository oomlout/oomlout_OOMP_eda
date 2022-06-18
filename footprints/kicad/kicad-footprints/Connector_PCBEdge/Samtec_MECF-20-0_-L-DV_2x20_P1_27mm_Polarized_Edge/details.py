###### OOMP FILE  ######

import OOMP

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "kicad")
newPart.addTag("oompColor", "kicad-footprints")
newPart.addTag("oompDesc", "Connector_PCBEdge")
newPart.addTag("oompIndex", "Samtec_MECF-20-0_-L-DV_2x20_P1.27mm_Polarized_Edge")

newPart.addTag("kicadDesc", "Highspeed card edge connector for PCB's with 20 contacts (polarized)")
newPart.addTag("kicadTags", "conn samtec card-edge high-speed")
newPart.addTag("kicadAttr", "exclude_from_pos_files exclude_from_bom")

OOMP.parts.append(newPart)