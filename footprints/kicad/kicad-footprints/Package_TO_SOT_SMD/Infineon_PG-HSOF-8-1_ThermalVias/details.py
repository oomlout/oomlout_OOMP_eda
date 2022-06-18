###### OOMP FILE  ######

import OOMP

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "kicad")
newPart.addTag("oompColor", "kicad-footprints")
newPart.addTag("oompDesc", "Package_TO_SOT_SMD")
newPart.addTag("oompIndex", "Infineon_PG-HSOF-8-1_ThermalVias")

newPart.addTag("kicadDesc", "HSOF-8-1 [TOLL] power MOSFET (http://www.infineon.com/cms/en/product/packages/PG-HSOF/PG-HSOF-8-1/)")
newPart.addTag("kicadTags", "mosfet hsof toll thermal vias")
newPart.addTag("kicadAttr", "smd")
newPart.addTag("kicad3DModel", "${KICAD6_3DMODEL_DIR}/Package_TO_SOT_SMD.3dshapes/Infineon_PG-HSOF-8-1.wrl")

OOMP.parts.append(newPart)