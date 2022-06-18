###### OOMP FILE  ######

import OOMP

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "kicad")
newPart.addTag("oompColor", "kicad-footprints")
newPart.addTag("oompDesc", "Package_LGA")
newPart.addTag("oompIndex", "LGA-16_3x3mm_P0.5mm")
newPart.addTag("oompName", "kicad-footprints/Package_LGA/LGA-16_3x3mm_P0.5mm")

newPart.addTag("kicadDesc", "http://www.memsic.com/userfiles/files/DataSheets/Magnetic-Sensors-Datasheets/MMC5883MA-RevC.pdf")
newPart.addTag("kicadTags", "lga land grid array")
newPart.addTag("kicadAttr", "smd")
newPart.addTag("kicad3DModel", "${KICAD6_3DMODEL_DIR}/Package_LGA.3dshapes/LGA-16_3x3mm_P0.5mm.wrl")

OOMP.parts.append(newPart)