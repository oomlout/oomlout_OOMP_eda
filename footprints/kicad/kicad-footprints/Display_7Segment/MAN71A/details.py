###### OOMP FILE  ######

import OOMP

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "kicad")
newPart.addTag("oompColor", "kicad-footprints")
newPart.addTag("oompDesc", "Display_7Segment")
newPart.addTag("oompIndex", "MAN71A")

newPart.addTag("kicadDesc", "https://www.digchip.com/datasheets/parts/datasheet/161/MAN3640A-pdf.php")
newPart.addTag("kicadTags", "One digit 7 segment red LED with right dot")
newPart.addTag("kicadAttr", "through_hole")
newPart.addTag("kicad3DModel", "${KICAD6_3DMODEL_DIR}/Display_7Segment.3dshapes/MAN71A.wrl")

OOMP.parts.append(newPart)