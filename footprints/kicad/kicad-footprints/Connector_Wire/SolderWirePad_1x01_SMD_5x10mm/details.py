###### OOMP FILE  ######

import OOMP

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "kicad")
newPart.addTag("oompColor", "kicad-footprints")
newPart.addTag("oompDesc", "Connector_Wire")
newPart.addTag("oompIndex", "SolderWirePad_1x01_SMD_5x10mm")

newPart.addTag("kicadDesc", "Wire Pad, Square, SMD Pad,  5mm x 10mm,")
newPart.addTag("kicadTags", "MesurementPoint Square SMDPad 5mmx10mm")
newPart.addTag("kicadAttr", "smd exclude_from_pos_files exclude_from_bom")

OOMP.parts.append(newPart)