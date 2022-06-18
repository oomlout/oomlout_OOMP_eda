###### OOMP FILE  ######

import OOMP

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "kicad")
newPart.addTag("oompColor", "kicad-footprints")
newPart.addTag("oompDesc", "Battery")
newPart.addTag("oompIndex", "BatteryHolder_LINX_BAT-HLD-012-SMT")

newPart.addTag("kicadDesc", "SMT battery holder for CR1216/1220/1225, https://linxtechnologies.com/wp/wp-content/uploads/bat-hld-012-smt.pdf")
newPart.addTag("kicadTags", "battery holder coin cell cr1216 cr1220 cr1225")
newPart.addTag("kicadAttr", "smd")
newPart.addTag("kicad3DModel", "${KICAD6_3DMODEL_DIR}/Battery.3dshapes/BatteryHolder_LINX_BAT-HLD-012-SMT.wrl")

OOMP.parts.append(newPart)