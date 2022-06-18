###### OOMP FILE  ######

import OOMP

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "kicad")
newPart.addTag("oompColor", "kicad-footprints")
newPart.addTag("oompDesc", "Fiducial")
newPart.addTag("oompIndex", "Fiducial_1.5mm_Mask3mm")

newPart.addTag("kicadDesc", "Circular Fiducial, 1.5mm bare copper, 3mm soldermask opening")
newPart.addTag("kicadTags", "fiducial")
newPart.addTag("kicadAttr", "smd")

OOMP.parts.append(newPart)