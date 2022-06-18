###### OOMP FILE  ######

import OOMP

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "kicad")
newPart.addTag("oompColor", "kicad-footprints")
newPart.addTag("oompDesc", "Fiducial")
newPart.addTag("oompIndex", "Fiducial_0.5mm_Mask1mm")

newPart.addTag("kicadDesc", "Circular Fiducial, 0.5mm bare copper, 1mm soldermask opening (Level C)")
newPart.addTag("kicadTags", "fiducial")
newPart.addTag("kicadAttr", "smd")

OOMP.parts.append(newPart)