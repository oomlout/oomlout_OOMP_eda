###### OOMP FILE  ######

import OOMP

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "kicad")
newPart.addTag("oompColor", "kicad-footprints")
newPart.addTag("oompDesc", "Battery")
newPart.addTag("oompIndex", "BatteryHolder_Keystone_2468_2xAAA")

newPart.addTag("kicadDesc", "2xAAA cell battery holder, Keystone P/N 2468, http://www.keyelco.com/product-pdf.cfm?p=1033")
newPart.addTag("kicadTags", "AAA battery cell holder")
newPart.addTag("kicadAttr", "through_hole")
newPart.addTag("kicad3DModel", "${KICAD6_3DMODEL_DIR}/Battery.3dshapes/BatteryHolder_Keystone_2468_2xAAA.wrl")

OOMP.parts.append(newPart)