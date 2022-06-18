###### OOMP FILE  ######

import OOMP

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "kicad")
newPart.addTag("oompColor", "kicad-footprints")
newPart.addTag("oompDesc", "Crystal")
newPart.addTag("oompIndex", "Resonator_Murata_CSTLSxxxG-3Pin_W8.0mm_H3.0mm")

newPart.addTag("kicadDesc", "Ceramic Resomator/Filter Murata CSTLSxxxG, http://www.murata.com/~/media/webrenewal/support/library/catalog/products/timingdevice/ceralock/p17e.ashx, length*width=8.0x3.0mm^2 package, package length=8.0mm, package width=3.0mm, 3 pins")
newPart.addTag("kicadTags", "THT ceramic resonator filter CSTLSxxxG")
newPart.addTag("kicadAttr", "through_hole")
newPart.addTag("kicad3DModel", "${KICAD6_3DMODEL_DIR}/Crystal.3dshapes/Resonator_Murata_CSTLSxxxG-3Pin_W8.0mm_H3.0mm.wrl")

OOMP.parts.append(newPart)