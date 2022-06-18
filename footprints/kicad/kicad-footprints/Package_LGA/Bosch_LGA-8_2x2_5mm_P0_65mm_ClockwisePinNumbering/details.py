###### OOMP FILE  ######

import OOMP

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "kicad")
newPart.addTag("oompColor", "kicad-footprints")
newPart.addTag("oompDesc", "Package_LGA")
newPart.addTag("oompIndex", "Bosch_LGA-8_2x2.5mm_P0.65mm_ClockwisePinNumbering")
newPart.addTag("oompName", "kicad-footprints/Package_LGA/Bosch_LGA-8_2x2.5mm_P0.65mm_ClockwisePinNumbering")

newPart.addTag("kicadDesc", "LGA-8, https://ae-bst.resource.bosch.com/media/_tech/media/datasheets/BST-BMP280-DS001-18.pdf")
newPart.addTag("kicadTags", "lga land grid array")
newPart.addTag("kicadAttr", "smd")
newPart.addTag("kicad3DModel", "${KICAD6_3DMODEL_DIR}/Package_LGA.3dshapes/Bosch_LGA-8_2x2.5mm_P0.65mm_ClockwisePinNumbering.wrl")

OOMP.parts.append(newPart)