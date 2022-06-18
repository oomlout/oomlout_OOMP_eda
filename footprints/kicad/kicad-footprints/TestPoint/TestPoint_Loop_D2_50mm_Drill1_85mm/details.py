###### OOMP FILE  ######

import OOMP

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "kicad")
newPart.addTag("oompColor", "kicad-footprints")
newPart.addTag("oompDesc", "TestPoint")
newPart.addTag("oompIndex", "TestPoint_Loop_D2.50mm_Drill1.85mm")
newPart.addTag("oompName", "kicad-footprints/TestPoint/TestPoint_Loop_D2.50mm_Drill1.85mm")

newPart.addTag("kicadDesc", "wire loop as test point, loop diameter 2.5mm, hole diameter 1.85mm")
newPart.addTag("kicadTags", "test point wire loop bead")
newPart.addTag("kicadAttr", "through_hole")
newPart.addTag("kicad3DModel", "${KICAD6_3DMODEL_DIR}/TestPoint.3dshapes/TestPoint_Loop_D2.50mm_Drill1.85mm.wrl")

OOMP.parts.append(newPart)