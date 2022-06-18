###### OOMP FILE  ######

import OOMP

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "kicad")
newPart.addTag("oompColor", "kicad-footprints")
newPart.addTag("oompDesc", "Battery")
newPart.addTag("oompIndex", "Battery_CR1225")
newPart.addTag("oompName", "kicad-footprints/Battery/Battery_CR1225")

newPart.addTag("kicadDesc", "CR1225 battery")
newPart.addTag("kicadTags", "battery CR1225 coin cell")
newPart.addTag("kicadAttr", "exclude_from_pos_files exclude_from_bom")
newPart.addTag("kicad3DModel", "${KICAD6_3DMODEL_DIR}/Battery.3dshapes/Battery_CR1225.wrl")

OOMP.parts.append(newPart)