###### OOMP FILE  ######

import OOMP

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "kicad")
newPart.addTag("oompColor", "kicad-footprints")
newPart.addTag("oompDesc", "Package_DIP")
newPart.addTag("oompIndex", "PowerIntegrations_SMD-8B")
newPart.addTag("oompName", "kicad-footprints/Package_DIP/PowerIntegrations_SMD-8B")

newPart.addTag("kicadDesc", "PowerIntegrations variant of 8-lead surface-mounted (SMD) DIP package, row spacing 7.62 mm (300 mils), see https://www.power.com/sites/default/files/product-docs/lnk520.pdf")
newPart.addTag("kicadTags", "SMD DIP DIL PDIP SMDIP 2.54mm 7.62mm 300mil")
newPart.addTag("kicadAttr", "smd")
newPart.addTag("kicad3DModel", "${KICAD6_3DMODEL_DIR}/Package_DIP.3dshapes/PowerIntegrations_SMD-8B.wrl")

OOMP.parts.append(newPart)