###### OOMP FILE  ######

import OOMP

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "kicad")
newPart.addTag("oompColor", "kicad-footprints")
newPart.addTag("oompDesc", "RF_Module")
newPart.addTag("oompIndex", "TD1205")

newPart.addTag("kicadDesc", "https://github.com/Telecom-Design/Documentation_TD_RF_Module/blob/master/TD1205%20Datasheet.pdf")
newPart.addTag("kicadTags", "SIGFOX Module")
newPart.addTag("kicadAttr", "through_hole")
newPart.addTag("kicad3DModel", "${KICAD6_3DMODEL_DIR}/RF_Module.3dshapes/TD1205.wrl")

OOMP.parts.append(newPart)