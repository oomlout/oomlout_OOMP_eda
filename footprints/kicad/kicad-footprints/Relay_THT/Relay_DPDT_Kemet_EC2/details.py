###### OOMP FILE  ######

import OOMP

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "kicad")
newPart.addTag("oompColor", "kicad-footprints")
newPart.addTag("oompDesc", "Relay_THT")
newPart.addTag("oompIndex", "Relay_DPDT_Kemet_EC2")

newPart.addTag("kicadDesc", "Kemet signal relay, DPDT, non-latching, single coil latching, https://content.kemet.com/datasheets/KEM_R7002_EC2_EE2.pdf")
newPart.addTag("kicadTags", "Kemet EC2 signal relay DPDT non single coil latching through hole THT")
newPart.addTag("kicadAttr", "through_hole")
newPart.addTag("kicad3DModel", "${KICAD6_3DMODEL_DIR}/Relay_THT.3dshapes/Relay_DPDT_Kemet_EC2.wrl")

OOMP.parts.append(newPart)