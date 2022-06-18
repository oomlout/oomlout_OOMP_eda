###### OOMP FILE  ######

import OOMP

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "kicad")
newPart.addTag("oompColor", "kicad-footprints")
newPart.addTag("oompDesc", "Connector_BarrelJack")
newPart.addTag("oompIndex", "BarrelJack_GCT_DCJ200-10-A_Horizontal")

newPart.addTag("kicadDesc", "Barrel jack connector (5.5 mm outer diameter, 2.05 inner diameter ), https://gct.co/files/drawings/dcj200-10.pdf")
newPart.addTag("kicadTags", "connector barrel jack")
newPart.addTag("kicadAttr", "through_hole")
newPart.addTag("kicad3DModel", "${KICAD6_3DMODEL_DIR}/Connector_BarrelJack.3dshapes/BarrelJack_GCT_DCJ200-10-A_Horizontal.wrl")

OOMP.parts.append(newPart)