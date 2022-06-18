###### OOMP FILE  ######

import OOMP

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "kicad")
newPart.addTag("oompColor", "kicad-footprints")
newPart.addTag("oompDesc", "Connector_Card")
newPart.addTag("oompIndex", "microSD_HC_Molex_104031-0811")

newPart.addTag("kicadDesc", "1.10mm Pitch microSD Memory Card Connector, Surface Mount, Push-Pull Type, 1.42mm Height, with Detect Switch (https://www.molex.com/pdm_docs/sd/1040310811_sd.pdf)")
newPart.addTag("kicadTags", "microSD SD molex")
newPart.addTag("kicadAttr", "smd")
newPart.addTag("kicad3DModel", "${KICAD6_3DMODEL_DIR}/Connector_Card.3dshapes/microSD_HC_Molex_104031-0811.wrl")

OOMP.parts.append(newPart)