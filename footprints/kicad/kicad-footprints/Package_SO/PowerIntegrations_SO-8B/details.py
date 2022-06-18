###### OOMP FILE  ######

import OOMP

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "kicad")
newPart.addTag("oompColor", "kicad-footprints")
newPart.addTag("oompDesc", "Package_SO")
newPart.addTag("oompIndex", "PowerIntegrations_SO-8B")

newPart.addTag("kicadDesc", "Power-Integrations variant of 8-Lead Plastic Small Outline (SN) - Narrow, 3.90 mm Body [SOIC], see https://www.mouser.com/ds/2/328/linkswitch-pl_family_datasheet-12517.pdf")
newPart.addTag("kicadTags", "SOIC 1.27")
newPart.addTag("kicadAttr", "smd")
newPart.addTag("kicad3DModel", "${KICAD6_3DMODEL_DIR}/Package_SO.3dshapes/PowerIntegrations_SO-8B.wrl")

OOMP.parts.append(newPart)