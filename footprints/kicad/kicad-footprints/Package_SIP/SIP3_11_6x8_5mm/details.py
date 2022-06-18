###### OOMP FILE  ######

import OOMP

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "kicad")
newPart.addTag("oompColor", "kicad-footprints")
newPart.addTag("oompDesc", "Package_SIP")
newPart.addTag("oompIndex", "SIP3_11.6x8.5mm")

newPart.addTag("kicadDesc", "RECOM,R78EXX,https://www.recom-power.com/pdf/Innoline/R-78Exx-0.5.pdf")
newPart.addTag("kicadTags", "SIP3 Regulator Module")
newPart.addTag("kicadAttr", "through_hole")
newPart.addTag("kicad3DModel", "${KICAD6_3DMODEL_DIR}/Package_SIP.3dshapes/SIP3_11.6x8.5mm.wrl")

OOMP.parts.append(newPart)