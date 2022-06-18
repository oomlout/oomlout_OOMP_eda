###### OOMP FILE  ######

import OOMP

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "kicad")
newPart.addTag("oompColor", "kicad-footprints")
newPart.addTag("oompDesc", "Inductor_THT")
newPart.addTag("oompIndex", "Choke_Schaffner_RN212-04-12.5x18.0mm")

newPart.addTag("kicadDesc", "Current-compensated Chokes, Schaffner, RN212-04, 12.5mmx18.0mm https://www.schaffner.com/products/download/product/datasheet/rn-series-common-mode-chokes-new/")
newPart.addTag("kicadTags", "chokes schaffner tht")
newPart.addTag("kicadAttr", "through_hole")
newPart.addTag("kicad3DModel", "${KICAD6_3DMODEL_DIR}/Inductor_THT.3dshapes/Choke_Schaffner_RN212-04-12.5x18.0mm.wrl")

OOMP.parts.append(newPart)