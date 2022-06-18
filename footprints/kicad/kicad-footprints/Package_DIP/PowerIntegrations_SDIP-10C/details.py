###### OOMP FILE  ######

import OOMP

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "kicad")
newPart.addTag("oompColor", "kicad-footprints")
newPart.addTag("oompDesc", "Package_DIP")
newPart.addTag("oompIndex", "PowerIntegrations_SDIP-10C")

newPart.addTag("kicadDesc", "PowerIntegrations variant of 10-lead though-hole mounted DIP package, row spacing 7.62 mm (300 mils), LongPads, see https://www.power.com/sites/default/files/product-docs/tophx_family_datasheet.pdf")
newPart.addTag("kicadTags", "THT DIP DIL PDIP 2.54mm 7.62mm 300mil LongPads")
newPart.addTag("kicadAttr", "through_hole")
newPart.addTag("kicad3DModel", "${KICAD6_3DMODEL_DIR}/Package_DIP.3dshapes/PowerIntegrations_SDIP-10C.wrl")

OOMP.parts.append(newPart)