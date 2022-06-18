###### OOMP FILE  ######

import OOMP

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "kicad")
newPart.addTag("oompColor", "kicad-footprints")
newPart.addTag("oompDesc", "Fiducial")
newPart.addTag("oompIndex", "Fiducial_1mm_Mask2mm")

newPart.addTag("kicadDesc", "Circular Fiducial, 1mm bare copper, 2mm soldermask opening (Level A)")
newPart.addTag("kicadTags", "fiducial")
newPart.addTag("kicadAttr", "smd")

OOMP.parts.append(newPart)