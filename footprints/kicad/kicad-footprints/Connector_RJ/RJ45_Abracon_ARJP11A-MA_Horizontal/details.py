###### OOMP FILE  ######

import OOMP

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "kicad")
newPart.addTag("oompColor", "kicad-footprints")
newPart.addTag("oompDesc", "Connector_RJ")
newPart.addTag("oompIndex", "RJ45_Abracon_ARJP11A-MA_Horizontal")

newPart.addTag("kicadDesc", "Shielded RJ45 ethernet connector with transformer and POE (https://abracon.com/Magnetics/lan/ARJP11A.PDF)")
newPart.addTag("kicadTags", "ethernet 8p8c transformer poe rj45")
newPart.addTag("kicadAttr", "through_hole")
newPart.addTag("kicad3DModel", "${KICAD6_3DMODEL_DIR}/Connector_RJ.3dshapes/RJ45_Abracon_ARJP11A-MA_Horizontal.wrl")

OOMP.parts.append(newPart)