###### OOMP FILE  ######

import OOMP

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "kicad")
newPart.addTag("oompColor", "kicad-footprints")
newPart.addTag("oompDesc", "Filter")
newPart.addTag("oompIndex", "Filter_Schaffner_FN405")

newPart.addTag("kicadDesc", "Compact PCB mounting EMI filter (https://www.schaffner.com/de/produkte/download/product/datasheet/fn-405-pcb-mounting-filter/)")
newPart.addTag("kicadTags", "EMI filter")
newPart.addTag("kicadAttr", "through_hole")
newPart.addTag("kicad3DModel", "${KICAD6_3DMODEL_DIR}/Filter.3dshapes/Filter_Schaffner_FN405.wrl")

OOMP.parts.append(newPart)