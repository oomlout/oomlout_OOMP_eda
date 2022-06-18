###### OOMP FILE  ######

import OOMP

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "kicad")
newPart.addTag("oompColor", "kicad-footprints")
newPart.addTag("oompDesc", "Fiducial")
newPart.addTag("oompIndex", "Fiducial_0.75mm_Mask2.25mm")

newPart.addTag("kicadDesc", "Circular Fiducial, 0.75mm bare copper, 2.25mm soldermask opening")
newPart.addTag("kicadTags", "fiducial")
newPart.addTag("kicadAttr", "smd")

OOMP.parts.append(newPart)