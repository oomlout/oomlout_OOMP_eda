###### OOMP FILE  ######

import OOMP

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "kicad")
newPart.addTag("oompColor", "kicad-footprints")
newPart.addTag("oompDesc", "Package_SO")
newPart.addTag("oompIndex", "Infineon_PG-DSO-20-87")

newPart.addTag("kicadDesc", "Infineon SO package 20pin without exposed pad (https://www.infineon.com/cms/en/product/packages/PG-DSO/PG-DSO-20-87/)")
newPart.addTag("kicadTags", "DSO-20")
newPart.addTag("kicadAttr", "smd")
newPart.addTag("kicad3DModel", "${KICAD6_3DMODEL_DIR}/Package_SO.3dshapes/Infineon_PG-DSO-20-87.wrl")

OOMP.parts.append(newPart)