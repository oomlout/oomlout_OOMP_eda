###### OOMP FILE  ######

import OOMP

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "kicad")
newPart.addTag("oompColor", "kicad-footprints")
newPart.addTag("oompDesc", "LED_SMD")
newPart.addTag("oompIndex", "LED-L1T2_LUMILEDS")

newPart.addTag("kicadDesc", "http://www.lumileds.com/uploads/438/DS133-pdf")
newPart.addTag("kicadTags", "LUMILEDS LUXEON TX L1T2 LED")
newPart.addTag("kicadAttr", "smd")
newPart.addTag("kicad3DModel", "${KICAD6_3DMODEL_DIR}/LED_SMD.3dshapes/LED-L1T2_LUMILEDS.wrl")

OOMP.parts.append(newPart)