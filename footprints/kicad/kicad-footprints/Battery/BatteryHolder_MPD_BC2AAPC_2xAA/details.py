###### OOMP FILE  ######

import OOMP

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "kicad")
newPart.addTag("oompColor", "kicad-footprints")
newPart.addTag("oompDesc", "Battery")
newPart.addTag("oompIndex", "BatteryHolder_MPD_BC2AAPC_2xAA")

newPart.addTag("kicadDesc", "2xAA cell battery holder, Memory Protection Devices P/N BC2AAPC, http://www.memoryprotectiondevices.com/datasheets/BC2AAPC-datasheet.pdf")
newPart.addTag("kicadTags", "AA battery cell holder")
newPart.addTag("kicadAttr", "through_hole")
newPart.addTag("kicad3DModel", "${KICAD6_3DMODEL_DIR}/Battery.3dshapes/BatteryHolder_MPD_BC2AAPC_2xAA.wrl")

OOMP.parts.append(newPart)