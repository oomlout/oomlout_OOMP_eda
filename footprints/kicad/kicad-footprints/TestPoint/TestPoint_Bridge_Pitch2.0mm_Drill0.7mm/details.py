###### OOMP FILE  ######

import OOMP

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "kicad")
newPart.addTag("oompColor", "kicad-footprints")
newPart.addTag("oompDesc", "TestPoint")
newPart.addTag("oompIndex", "TestPoint_Bridge_Pitch2.0mm_Drill0.7mm")
newPart.addTag("oompName", "kicad-footprints/TestPoint/TestPoint_Bridge_Pitch2.0mm_Drill0.7mm")

newPart.addTag("kicadDesc", "wire loop as test point, pitch 2.0mm, hole diameter 0.7mm, wire diameter 0.5mm")
newPart.addTag("kicadTags", "test point wire loop")
newPart.addTag("kicadAttr", "through_hole")
newPart.addTag("kicad3DModel", "${KICAD6_3DMODEL_DIR}/TestPoint.3dshapes/TestPoint_Bridge_Pitch2.0mm_Drill0.7mm.wrl")

OOMP.parts.append(newPart)