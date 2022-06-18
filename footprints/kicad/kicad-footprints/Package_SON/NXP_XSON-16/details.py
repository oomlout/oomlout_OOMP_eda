###### OOMP FILE  ######

import OOMP

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "kicad")
newPart.addTag("oompColor", "kicad-footprints")
newPart.addTag("oompDesc", "Package_SON")
newPart.addTag("oompIndex", "NXP_XSON-16")

newPart.addTag("kicadDesc", "http://www.nxp.com/documents/outline_drawing/SOT1341-1.pdf")
newPart.addTag("kicadTags", "NXP XSON SOT-1341")
newPart.addTag("kicadAttr", "smd")
newPart.addTag("kicad3DModel", "${KICAD6_3DMODEL_DIR}/Package_SON.3dshapes/NXP_XSON-16.wrl")

OOMP.parts.append(newPart)