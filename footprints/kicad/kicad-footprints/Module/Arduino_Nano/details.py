###### OOMP FILE  ######

import OOMP

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "kicad")
newPart.addTag("oompColor", "kicad-footprints")
newPart.addTag("oompDesc", "Module")
newPart.addTag("oompIndex", "Arduino_Nano")

newPart.addTag("kicadDesc", "Arduino Nano, http://www.mouser.com/pdfdocs/Gravitech_Arduino_Nano3_0.pdf")
newPart.addTag("kicadTags", "Arduino Nano")
newPart.addTag("kicadAttr", "through_hole")
newPart.addTag("kicad3DModel", "${KICAD6_3DMODEL_DIR}/Module.3dshapes/Arduino_Nano_WithMountingHoles.wrl")

OOMP.parts.append(newPart)