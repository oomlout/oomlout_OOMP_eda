###### OOMP FILE  ######

import OOMP

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "kicad")
newPart.addTag("oompColor", "kicad-footprints")
newPart.addTag("oompDesc", "Display_7Segment")
newPart.addTag("oompIndex", "DE122-XX-XX")

newPart.addTag("kicadDesc", "http://www.display-elektronik.de/filter/DE122-RS-20_635.pdf")
newPart.addTag("kicadTags", "6 digit 7 segment LCD")
newPart.addTag("kicadAttr", "through_hole")
newPart.addTag("kicad3DModel", "${KICAD6_3DMODEL_DIR}/Display_7Segment.3dshapes/DE122-XX-XX.wrl")

OOMP.parts.append(newPart)