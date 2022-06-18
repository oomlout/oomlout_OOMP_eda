###### OOMP FILE  ######

import OOMP

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "kicad")
newPart.addTag("oompColor", "kicad-footprints")
newPart.addTag("oompDesc", "Battery")
newPart.addTag("oompIndex", "BatteryHolder_MPD_BH-18650-PC2")

newPart.addTag("kicadDesc", "18650 Battery Holder (http://www.memoryprotectiondevices.com/datasheets/BK-18650-PC2-datasheet.pdf)")
newPart.addTag("kicadTags", "18650 Battery Holder")
newPart.addTag("kicadAttr", "through_hole")
newPart.addTag("kicad3DModel", "${KICAD6_3DMODEL_DIR}/Battery.3dshapes/BatteryHolder_MPD_BH-18650-PC2.wrl")

OOMP.parts.append(newPart)