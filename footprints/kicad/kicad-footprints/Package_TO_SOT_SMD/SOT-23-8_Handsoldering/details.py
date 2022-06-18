###### OOMP FILE  ######

import OOMP

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "kicad")
newPart.addTag("oompColor", "kicad-footprints")
newPart.addTag("oompDesc", "Package_TO_SOT_SMD")
newPart.addTag("oompIndex", "SOT-23-8_Handsoldering")

newPart.addTag("kicadDesc", "8-pin SOT-23 package, Handsoldering, http://www.analog.com/media/en/package-pcb-resources/package/pkg_pdf/sot-23rj/rj_8.pdf")
newPart.addTag("kicadTags", "SOT-23-8 Handsoldering")
newPart.addTag("kicadAttr", "smd")
newPart.addTag("kicad3DModel", "${KICAD6_3DMODEL_DIR}/Package_TO_SOT_SMD.3dshapes/SOT-23-8.wrl")

OOMP.parts.append(newPart)