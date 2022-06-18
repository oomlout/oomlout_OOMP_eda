###### OOMP FILE  ######

import OOMP

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "kicad")
newPart.addTag("oompColor", "kicad-footprints")
newPart.addTag("oompDesc", "Relay_THT")
newPart.addTag("oompIndex", "Relay_DPDT_Omron_G6H-2")

newPart.addTag("kicadDesc", "Omron relay G6H-2, see http://cdn-reichelt.de/documents/datenblatt/C300/G6H%23OMR.pdf")
newPart.addTag("kicadTags", "Omron relay G6H-2")
newPart.addTag("kicadAttr", "through_hole")
newPart.addTag("kicad3DModel", "${KICAD6_3DMODEL_DIR}/Relay_THT.3dshapes/Relay_DPDT_Omron_G6H-2.wrl")

OOMP.parts.append(newPart)