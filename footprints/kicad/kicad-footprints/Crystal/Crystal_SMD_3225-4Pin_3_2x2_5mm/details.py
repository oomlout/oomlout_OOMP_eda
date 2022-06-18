###### OOMP FILE  ######

import OOMP

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "kicad")
newPart.addTag("oompColor", "kicad-footprints")
newPart.addTag("oompDesc", "Crystal")
newPart.addTag("oompIndex", "Crystal_SMD_3225-4Pin_3.2x2.5mm")

newPart.addTag("kicadDesc", "SMD Crystal SERIES SMD3225/4 http://www.txccrystal.com/images/pdf/7m-accuracy.pdf, 3.2x2.5mm^2 package")
newPart.addTag("kicadTags", "SMD SMT crystal")
newPart.addTag("kicadAttr", "smd")
newPart.addTag("kicad3DModel", "${KICAD6_3DMODEL_DIR}/Crystal.3dshapes/Crystal_SMD_3225-4Pin_3.2x2.5mm.wrl")

OOMP.parts.append(newPart)