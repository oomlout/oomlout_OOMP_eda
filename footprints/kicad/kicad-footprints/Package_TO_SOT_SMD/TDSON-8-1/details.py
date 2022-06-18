###### OOMP FILE  ######

import OOMP

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "kicad")
newPart.addTag("oompColor", "kicad-footprints")
newPart.addTag("oompDesc", "Package_TO_SOT_SMD")
newPart.addTag("oompIndex", "TDSON-8-1")

newPart.addTag("kicadDesc", "Power MOSFET package, TDSON-8-1, 5.15x5.9mm (https://www.infineon.com/cms/en/product/packages/PG-TDSON/PG-TDSON-8-1/)")
newPart.addTag("kicadTags", "tdson")
newPart.addTag("kicadAttr", "smd")
newPart.addTag("kicad3DModel", "${KICAD6_3DMODEL_DIR}/Package_TO_SOT_SMD.3dshapes/TDSON-8-1.wrl")

OOMP.parts.append(newPart)