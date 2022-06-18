###### OOMP FILE  ######

import OOMP

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "kicad")
newPart.addTag("oompColor", "kicad-footprints")
newPart.addTag("oompDesc", "Package_SO")
newPart.addTag("oompIndex", "Infineon_PG-DSO-12-11")

newPart.addTag("kicadDesc", "Infineon PG-DSO 12 pin, exposed pad: 4.5x8.1mm, with thermal vias (https://www.infineon.com/cms/en/product/packages/PG-DSO/PG-DSO-12-11/)")
newPart.addTag("kicadTags", "PG-DSO")
newPart.addTag("kicadAttr", "smd")
newPart.addTag("kicad3DModel", "${KICAD6_3DMODEL_DIR}/Package_SO.3dshapes/Infineon_PG-DSO-12-11.wrl")

OOMP.parts.append(newPart)