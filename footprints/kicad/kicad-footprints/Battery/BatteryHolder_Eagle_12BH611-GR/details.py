###### OOMP FILE  ######

import OOMP

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "kicad")
newPart.addTag("oompColor", "kicad-footprints")
newPart.addTag("oompDesc", "Battery")
newPart.addTag("oompIndex", "BatteryHolder_Eagle_12BH611-GR")

newPart.addTag("kicadDesc", "https://eu.mouser.com/datasheet/2/209/EPD-200766-1274481.pdf")
newPart.addTag("kicadTags", "9V Battery Holder")
newPart.addTag("kicadAttr", "through_hole")
newPart.addTag("kicad3DModel", "${KICAD6_3DMODEL_DIR}/Battery.3dshapes/BatteryHolder_Eagle_12BH611-GR.wrl")

OOMP.parts.append(newPart)