###### OOMP FILE  ######

import OOMP

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "kicad")
newPart.addTag("oompColor", "kicad-footprints")
newPart.addTag("oompDesc", "Crystal")
newPart.addTag("oompIndex", "Crystal_SMD_0603-4Pin_6.0x3.5mm")

newPart.addTag("kicadDesc", "SMD Crystal SERIES SMD0603/4 http://www.petermann-technik.de/fileadmin/petermann/pdf/SMD0603-4.pdf, 6.0x3.5mm^2 package")
newPart.addTag("kicadTags", "SMD SMT crystal")
newPart.addTag("kicadAttr", "smd")
newPart.addTag("kicad3DModel", "${KICAD6_3DMODEL_DIR}/Crystal.3dshapes/Crystal_SMD_0603-4Pin_6.0x3.5mm.wrl")

OOMP.parts.append(newPart)