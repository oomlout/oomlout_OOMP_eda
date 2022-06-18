###### OOMP FILE  ######

import OOMP

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "kicad")
newPart.addTag("oompColor", "kicad-footprints")
newPart.addTag("oompDesc", "Connector_RJ")
newPart.addTag("oompIndex", "RJ45_Pulse_JK0654219NL_Horizontal")

newPart.addTag("kicadDesc", "10/100/1000 Base-T RJ45 single port with LEDs https://media.digikey.com/pdf/Data%20Sheets/Pulse%20PDFs/JK%20Series.pdf#page=2")
newPart.addTag("kicadTags", "RJ45 8p8c ethernet")
newPart.addTag("kicadAttr", "through_hole")
newPart.addTag("kicad3DModel", "${KICAD6_3DMODEL_DIR}/Connector_RJ.3dshapes/RJ45_Pulse_JK0654219NL_Horizontal.wrl")

OOMP.parts.append(newPart)