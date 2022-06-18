###### OOMP FILE  ######

import OOMP

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "kicad")
newPart.addTag("oompColor", "kicad-footprints")
newPart.addTag("oompDesc", "Package_LGA")
newPart.addTag("oompIndex", "Bosch_LGA-14_3x2.5mm_P0.5mm")

newPart.addTag("kicadDesc", "LGA-14 Bosch https://ae-bst.resource.bosch.com/media/_tech/media/datasheets/BST-BMI160-DS000-07.pdf")
newPart.addTag("kicadTags", "lga land grid array")
newPart.addTag("kicadAttr", "smd")
newPart.addTag("kicad3DModel", "${KICAD6_3DMODEL_DIR}/Package_LGA.3dshapes/Bosch_LGA-14_3x2.5mm_P0.5mm.wrl")

OOMP.parts.append(newPart)