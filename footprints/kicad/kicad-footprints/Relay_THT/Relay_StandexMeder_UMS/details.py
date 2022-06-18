###### OOMP FILE  ######

import OOMP

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "kicad")
newPart.addTag("oompColor", "kicad-footprints")
newPart.addTag("oompDesc", "Relay_THT")
newPart.addTag("oompIndex", "Relay_StandexMeder_UMS")

newPart.addTag("kicadDesc", "Standex-Meder SIL-relais, UMS, see http://cdn-reichelt.de/documents/datenblatt/C300/UMS05_1A80_75L_DB.pdf")
newPart.addTag("kicadTags", "Standex Meder SIL reed relais")
newPart.addTag("kicadAttr", "through_hole")
newPart.addTag("kicad3DModel", "${KICAD6_3DMODEL_DIR}/Relay_THT.3dshapes/Relay_StandexMeder_UMS.wrl")

OOMP.parts.append(newPart)