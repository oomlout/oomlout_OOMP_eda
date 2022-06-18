###### OOMP FILE  ######

import OOMP

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "kicad")
newPart.addTag("oompColor", "kicad-footprints")
newPart.addTag("oompDesc", "Connector_Audio")
newPart.addTag("oompIndex", "Jack_3.5mm_PJ320D_Horizontal")

newPart.addTag("kicadDesc", "Headphones with microphone connector, 3.5mm, 4 pins (http://www.qingpu-electronics.com/en/products/WQP-PJ320D-72.html)")
newPart.addTag("kicadTags", "3.5mm jack mic microphone phones headphones 4pins audio plug")
newPart.addTag("kicadAttr", "smd")
newPart.addTag("kicad3DModel", "${KICAD6_3DMODEL_DIR}/Connector_Audio.3dshapes/Jack_3.5mm_PJ320D_Horizontal.wrl")

OOMP.parts.append(newPart)