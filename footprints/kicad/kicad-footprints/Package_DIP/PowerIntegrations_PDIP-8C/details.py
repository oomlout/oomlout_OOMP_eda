###### OOMP FILE  ######

import OOMP

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "kicad")
newPart.addTag("oompColor", "kicad-footprints")
newPart.addTag("oompDesc", "Package_DIP")
newPart.addTag("oompIndex", "PowerIntegrations_PDIP-8C")

newPart.addTag("kicadDesc", "Power Integrations variant of 8-lead though-hole mounted DIP package, row spacing 7.62 mm (300 mils), LongPads, see https://ac-dc.power.com/sites/default/files/product-docs/tinyswitch-iii_family_datasheet.pdf")
newPart.addTag("kicadTags", "THT DIP DIL PDIP 2.54mm 7.62mm 300mil LongPads")
newPart.addTag("kicadAttr", "through_hole")
newPart.addTag("kicad3DModel", "${KICAD6_3DMODEL_DIR}/Package_DIP.3dshapes/PowerIntegrations_PDIP-8C.wrl")

OOMP.parts.append(newPart)