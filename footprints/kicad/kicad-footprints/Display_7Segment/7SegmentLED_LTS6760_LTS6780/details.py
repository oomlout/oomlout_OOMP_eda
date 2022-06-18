###### OOMP FILE  ######

import OOMP

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "kicad")
newPart.addTag("oompColor", "kicad-footprints")
newPart.addTag("oompDesc", "Display_7Segment")
newPart.addTag("oompIndex", "7SegmentLED_LTS6760_LTS6780")

newPart.addTag("kicadDesc", "7-Segment Display, LTS67x0, http://optoelectronics.liteon.com/upload/download/DS30-2001-355/S6760jd.pdf")
newPart.addTag("kicadTags", "7Segment LED LTS6760 LTS6780")
newPart.addTag("kicadAttr", "through_hole")
newPart.addTag("kicad3DModel", "${KICAD6_3DMODEL_DIR}/Display_7Segment.3dshapes/7SegmentLED_LTS6760_LTS6780.wrl")

OOMP.parts.append(newPart)