###### OOMP FILE  ######

import OOMP

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "kicad")
newPart.addTag("oompColor", "kicad-footprints")
newPart.addTag("oompDesc", "Crystal")
newPart.addTag("oompIndex", "Resonator-3Pin_W8.0mm_H3.5mm")

newPart.addTag("kicadDesc", "Ceramic Resomator/Filter 8.0x3.5mm^2, length*width=8.0x3.5mm^2 package, package length=8.0mm, package width=3.5mm, 3 pins")
newPart.addTag("kicadTags", "THT ceramic resonator filter")
newPart.addTag("kicadAttr", "through_hole")
newPart.addTag("kicad3DModel", "${KICAD6_3DMODEL_DIR}/Crystal.3dshapes/Resonator-3Pin_W8.0mm_H3.5mm.wrl")

OOMP.parts.append(newPart)