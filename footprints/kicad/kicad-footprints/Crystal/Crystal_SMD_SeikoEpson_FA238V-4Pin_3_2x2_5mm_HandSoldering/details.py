###### OOMP FILE  ######

import OOMP

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "kicad")
newPart.addTag("oompColor", "kicad-footprints")
newPart.addTag("oompDesc", "Crystal")
newPart.addTag("oompIndex", "Crystal_SMD_SeikoEpson_FA238V-4Pin_3.2x2.5mm_HandSoldering")

newPart.addTag("kicadDesc", "crystal Epson Toyocom FA-238 series http://www.mouser.com/ds/2/137/1721499-465440.pdf, hand-soldering, 3.2x2.5mm^2 package")
newPart.addTag("kicadTags", "SMD SMT crystal hand-soldering")
newPart.addTag("kicadAttr", "smd")
newPart.addTag("kicad3DModel", "${KICAD6_3DMODEL_DIR}/Crystal.3dshapes/Crystal_SMD_SeikoEpson_FA238V-4Pin_3.2x2.5mm_HandSoldering.wrl")

OOMP.parts.append(newPart)