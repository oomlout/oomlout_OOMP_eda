###### OOMP FILE  ######

import OOMP

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "kicad")
newPart.addTag("oompColor", "kicad-footprints")
newPart.addTag("oompDesc", "Inductor_THT")
newPart.addTag("oompIndex", "Choke_Schaffner_RN202-04-8.8x18.2mm")

newPart.addTag("kicadDesc", "Current-compensated Chokes, Schaffner, RN202-04, 8.8mmx18.2mm https://www.schaffner.com/products/download/product/datasheet/rn-series-common-mode-chokes-new/")
newPart.addTag("kicadTags", "chokes schaffner tht")
newPart.addTag("kicadAttr", "through_hole")
newPart.addTag("kicad3DModel", "${KICAD6_3DMODEL_DIR}/Inductor_THT.3dshapes/Choke_Schaffner_RN202-04-8.8x18.2mm.wrl")

OOMP.parts.append(newPart)