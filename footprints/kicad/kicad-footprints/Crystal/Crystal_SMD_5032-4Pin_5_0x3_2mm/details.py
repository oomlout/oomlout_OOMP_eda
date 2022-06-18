###### OOMP FILE  ######

import OOMP

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "kicad")
newPart.addTag("oompColor", "kicad-footprints")
newPart.addTag("oompDesc", "Crystal")
newPart.addTag("oompIndex", "Crystal_SMD_5032-4Pin_5.0x3.2mm")

newPart.addTag("kicadDesc", "SMD Crystal SERIES SMD2520/4 http://www.icbase.com/File/PDF/HKC/HKC00061008.pdf, 5.0x3.2mm^2 package")
newPart.addTag("kicadTags", "SMD SMT crystal")
newPart.addTag("kicadAttr", "smd")
newPart.addTag("kicad3DModel", "${KICAD6_3DMODEL_DIR}/Crystal.3dshapes/Crystal_SMD_5032-4Pin_5.0x3.2mm.wrl")

OOMP.parts.append(newPart)