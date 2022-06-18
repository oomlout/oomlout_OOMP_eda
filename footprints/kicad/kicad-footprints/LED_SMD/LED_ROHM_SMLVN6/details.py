###### OOMP FILE  ######

import OOMP

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "kicad")
newPart.addTag("oompColor", "kicad-footprints")
newPart.addTag("oompDesc", "LED_SMD")
newPart.addTag("oompIndex", "LED_ROHM_SMLVN6")

newPart.addTag("kicadDesc", "https://www.rohm.com/datasheet/SMLVN6RGB1U")
newPart.addTag("kicadTags", "LED ROHM SMLVN6")
newPart.addTag("kicadAttr", "smd")
newPart.addTag("kicad3DModel", "${KICAD6_3DMODEL_DIR}/LED_SMD.3dshapes/LED_ROHM_SMLVN6.wrl")

OOMP.parts.append(newPart)