###### OOMP FILE  ######

import OOMP

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "kicad")
newPart.addTag("oompColor", "kicad-footprints")
newPart.addTag("oompDesc", "Display_7Segment")
newPart.addTag("oompIndex", "DE119-XX-XX")

newPart.addTag("kicadDesc", "https://www.display-elektronik.de/filter/DE119-RS-20_635.pdf")
newPart.addTag("kicadTags", "4 digit 7 segment LCD")
newPart.addTag("kicadAttr", "through_hole")
newPart.addTag("kicad3DModel", "${KICAD6_3DMODEL_DIR}/Display_7Segment.3dshapes/DE119-XX-XX.wrl")

OOMP.parts.append(newPart)