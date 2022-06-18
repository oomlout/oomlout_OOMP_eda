###### OOMP FILE  ######

import OOMP

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "kicad")
newPart.addTag("oompColor", "kicad-footprints")
newPart.addTag("oompDesc", "Calibration_Scale")
newPart.addTag("oompIndex", "Gauge_100mm_Type2_SilkScreenTop")

newPart.addTag("kicadDesc", "Gauge, Massstab, 100mm, SilkScreenTop, Type 2,")
newPart.addTag("kicadTags", "Gauge Massstab 100mm SilkScreenTop Type 2")
newPart.addTag("kicadAttr", "exclude_from_pos_files exclude_from_bom")

OOMP.parts.append(newPart)