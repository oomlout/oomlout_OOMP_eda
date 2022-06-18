###### OOMP FILE  ######

import OOMP

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "kicad")
newPart.addTag("oompColor", "kicad-footprints")
newPart.addTag("oompDesc", "Relay_SMD")
newPart.addTag("oompIndex", "Relay_DPDT_Omron_G6H-2F")

newPart.addTag("kicadDesc", "package for Omron G6H-2F relais, see http://cdn-reichelt.de/documents/datenblatt/C300/G6H%23OMR.pdf")
newPart.addTag("kicadTags", "Omron G6H-2F relais")
newPart.addTag("kicadAttr", "smd")
newPart.addTag("kicad3DModel", "${KICAD6_3DMODEL_DIR}/Relay_SMD.3dshapes/Relay_DPDT_Omron_G6H-2F.wrl")

OOMP.parts.append(newPart)