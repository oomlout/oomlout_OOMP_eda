###### OOMP FILE  ######

import OOMP

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "kicad")
newPart.addTag("oompColor", "kicad-footprints")
newPart.addTag("oompDesc", "Connector_Audio")
newPart.addTag("oompIndex", "Jack_3.5mm_Switronic_ST-005-G_horizontal")

newPart.addTag("kicadDesc", "3.5mm horizontal headphones jack, http://akizukidenshi.com/download/ds/switronic/ST-005-G.pdf")
newPart.addTag("kicadTags", "Connector Audio Switronic ST-005-G")
newPart.addTag("kicadAttr", "through_hole")
newPart.addTag("kicad3DModel", "${KICAD6_3DMODEL_DIR}/Connector_Audio.3dshapes/Jack_3.5mm_Switronic_ST-005-G_horizontal.wrl")

OOMP.parts.append(newPart)