###### OOMP FILE  ######

import OOMP

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "kicad")
newPart.addTag("oompColor", "kicad-footprints")
newPart.addTag("oompDesc", "Package_SO")
newPart.addTag("oompIndex", "OnSemi_Micro8")

newPart.addTag("kicadDesc", "ON Semiconductor Micro8 (Case846A-02): https://www.onsemi.com/pub/Collateral/846A-02.PDF")
newPart.addTag("kicadTags", "micro8")
newPart.addTag("kicadAttr", "smd")
newPart.addTag("kicad3DModel", "${KICAD6_3DMODEL_DIR}/Package_SO.3dshapes/OnSemi_Micro8.wrl")

OOMP.parts.append(newPart)