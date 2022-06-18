###### OOMP FILE  ######

import OOMP

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "kicad")
newPart.addTag("oompColor", "kicad-footprints")
newPart.addTag("oompDesc", "Battery")
newPart.addTag("oompIndex", "BatteryHolder_Keystone_3000_1x12mm")

newPart.addTag("kicadDesc", "http://www.keyelco.com/product-pdf.cfm?p=777")
newPart.addTag("kicadTags", "Keystone type 3000 coin cell retainer")
newPart.addTag("kicadAttr", "smd")
newPart.addTag("kicad3DModel", "${KICAD6_3DMODEL_DIR}/Battery.3dshapes/BatteryHolder_Keystone_3000_1x12mm.wrl")

OOMP.parts.append(newPart)