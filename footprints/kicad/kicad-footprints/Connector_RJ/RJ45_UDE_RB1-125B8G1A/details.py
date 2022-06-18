###### OOMP FILE  ######

import OOMP

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "kicad")
newPart.addTag("oompColor", "kicad-footprints")
newPart.addTag("oompDesc", "Connector_RJ")
newPart.addTag("oompIndex", "RJ45_UDE_RB1-125B8G1A")

newPart.addTag("kicadDesc", "1 Port RJ45 Connector Through Hole 10/100/1000 Base-T, https://datasheet.lcsc.com/szlcsc/1901091107_UDE-Corp-RB1-125B8G1A_C363353.pdf#page=3")
newPart.addTag("kicadTags", "RJ45 ethernet")
newPart.addTag("kicadAttr", "through_hole")
newPart.addTag("kicad3DModel", "${KICAD6_3DMODEL_DIR}/Connector_RJ.3dshapes/RJ45_UDE_RB1-125B8G1A.wrl")

OOMP.parts.append(newPart)