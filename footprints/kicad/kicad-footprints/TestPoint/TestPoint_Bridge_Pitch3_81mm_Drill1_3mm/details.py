###### OOMP FILE  ######

import OOMP

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "kicad")
newPart.addTag("oompColor", "kicad-footprints")
newPart.addTag("oompDesc", "TestPoint")
newPart.addTag("oompIndex", "TestPoint_Bridge_Pitch3.81mm_Drill1.3mm")
newPart.addTag("oompName", "kicad-footprints/TestPoint/TestPoint_Bridge_Pitch3.81mm_Drill1.3mm")

newPart.addTag("kicadDesc", "wire loop as test point, pitch 3.81mm, hole diameter 1.3mm, wire diameter 1.0mm")
newPart.addTag("kicadTags", "test point wire loop")
newPart.addTag("kicadAttr", "through_hole")
newPart.addTag("kicad3DModel", "${KICAD6_3DMODEL_DIR}/TestPoint.3dshapes/TestPoint_Bridge_Pitch3.81mm_Drill1.3mm.wrl")

OOMP.parts.append(newPart)