###### OOMP FILE  ######

import OOMP

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "kicad")
newPart.addTag("oompColor", "kicad-footprints")
newPart.addTag("oompDesc", "Battery")
newPart.addTag("oompIndex", "BatteryHolder_Keystone_105_1x2430")

newPart.addTag("kicadDesc", "http://www.keyelco.com/product-pdf.cfm?p=745")
newPart.addTag("kicadTags", "Keystone type 105 battery holder")
newPart.addTag("kicadAttr", "through_hole")
newPart.addTag("kicad3DModel", "${KICAD6_3DMODEL_DIR}/Battery.3dshapes/BatteryHolder_Keystone_105_1x2430.wrl")

OOMP.parts.append(newPart)