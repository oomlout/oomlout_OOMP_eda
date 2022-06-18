###### OOMP FILE  ######

import OOMP

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "kicad")
newPart.addTag("oompColor", "kicad-footprints")
newPart.addTag("oompDesc", "TestPoint")
newPart.addTag("oompIndex", "TestPoint_Loop_D2.60mm_Drill1.4mm_Beaded")

newPart.addTag("kicadDesc", "wire loop with bead as test point, loop diameter2.6mm, hole diameter 1.4mm")
newPart.addTag("kicadTags", "test point wire loop bead")
newPart.addTag("kicadAttr", "through_hole")
newPart.addTag("kicad3DModel", "${KICAD6_3DMODEL_DIR}/TestPoint.3dshapes/TestPoint_Loop_D2.60mm_Drill1.4mm_Beaded.wrl")

OOMP.parts.append(newPart)