###### OOMP FILE  ######

import OOMP

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "kicad")
newPart.addTag("oompColor", "kicad-footprints")
newPart.addTag("oompDesc", "Module")
newPart.addTag("oompIndex", "Onion_Omega2S")

newPart.addTag("kicadDesc", "https://github.com/OnionIoT/Omega2/raw/master/Documents/Omega2S%20Datasheet.pdf")
newPart.addTag("kicadTags", "onion omega module")
newPart.addTag("kicadAttr", "smd")
newPart.addTag("kicad3DModel", "${KICAD6_3DMODEL_DIR}/Module.3dshapes/Onion_Omega2S.wrl")

OOMP.parts.append(newPart)