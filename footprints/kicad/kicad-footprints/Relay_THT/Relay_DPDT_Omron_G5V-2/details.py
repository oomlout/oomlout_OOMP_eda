###### OOMP FILE  ######

import OOMP

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "kicad")
newPart.addTag("oompColor", "kicad-footprints")
newPart.addTag("oompDesc", "Relay_THT")
newPart.addTag("oompIndex", "Relay_DPDT_Omron_G5V-2")

newPart.addTag("kicadDesc", "http://omronfs.omron.com/en_US/ecb/products/pdf/en-g5v2.pdf")
newPart.addTag("kicadTags", "Omron G5V-2 Relay DPDT")
newPart.addTag("kicadAttr", "through_hole")
newPart.addTag("kicad3DModel", "${KICAD6_3DMODEL_DIR}/Relay_THT.3dshapes/Relay_DPDT_Omron_G5V-2.wrl")

OOMP.parts.append(newPart)