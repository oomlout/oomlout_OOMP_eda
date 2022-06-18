###### OOMP FILE  ######

import OOMP

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "kicad")
newPart.addTag("oompColor", "kicad-footprints")
newPart.addTag("oompDesc", "RF_Antenna")
newPart.addTag("oompIndex", "Pulse_W3011")

newPart.addTag("kicadDesc", "Pulse RF Antenna, 4mm Clearance")
newPart.addTag("kicadTags", "antenna rf")
newPart.addTag("kicadAttr", "smd")
newPart.addTag("kicad3DModel", "${KICAD6_3DMODEL_DIR}/RF_Antenna.3dshapes/Pulse_W3011.wrl")

OOMP.parts.append(newPart)