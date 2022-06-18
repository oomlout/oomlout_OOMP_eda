###### OOMP FILE  ######

import OOMP

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "kicad")
newPart.addTag("oompColor", "kicad-footprints")
newPart.addTag("oompDesc", "Battery")
newPart.addTag("oompIndex", "BatteryHolder_MPD_BC2003_1x2032")

newPart.addTag("kicadDesc", "http://www.memoryprotectiondevices.com/datasheets/BC-2003-datasheet.pdf")
newPart.addTag("kicadTags", "BC2003 CR2032 2032 Battery Holder")
newPart.addTag("kicadAttr", "smd")
newPart.addTag("kicad3DModel", "${KICAD6_3DMODEL_DIR}/Battery.3dshapes/BatteryHolder_MPD_BC2003_1x2032.wrl")

OOMP.parts.append(newPart)