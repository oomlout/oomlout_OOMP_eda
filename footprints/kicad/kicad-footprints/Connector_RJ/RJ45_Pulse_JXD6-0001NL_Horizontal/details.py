###### OOMP FILE  ######

import OOMP

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "kicad")
newPart.addTag("oompColor", "kicad-footprints")
newPart.addTag("oompDesc", "Connector_RJ")
newPart.addTag("oompIndex", "RJ45_Pulse_JXD6-0001NL_Horizontal")

newPart.addTag("kicadDesc", "RJ45 ethernet transformer with magnetics (https://productfinder.pulseeng.com/doc_type/WEB301/doc_num/JXD6-0001NL/doc_part/JXD6-0001NL.pdf)")
newPart.addTag("kicadTags", "ethernet 8p8c transformer magjack")
newPart.addTag("kicadAttr", "smd")
newPart.addTag("kicad3DModel", "${KICAD6_3DMODEL_DIR}/Connector_RJ.3dshapes/RJ45_Pulse_JXD6-0001NL_Horizontal.wrl")

OOMP.parts.append(newPart)