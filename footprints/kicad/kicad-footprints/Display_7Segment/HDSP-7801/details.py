###### OOMP FILE  ######

import OOMP

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "kicad")
newPart.addTag("oompColor", "kicad-footprints")
newPart.addTag("oompDesc", "Display_7Segment")
newPart.addTag("oompIndex", "HDSP-7801")

newPart.addTag("kicadDesc", "One digit 7 segment green, https://docs.broadcom.com/docs/AV02-2553EN")
newPart.addTag("kicadTags", "One digit 7 segment green")
newPart.addTag("kicadAttr", "through_hole")
newPart.addTag("kicad3DModel", "${KICAD6_3DMODEL_DIR}/Display_7Segment.3dshapes/HDSP-7801.wrl")

OOMP.parts.append(newPart)