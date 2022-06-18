###### OOMP FILE  ######

import OOMP

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "kicad")
newPart.addTag("oompColor", "kicad-footprints")
newPart.addTag("oompDesc", "Relay_THT")
newPart.addTag("oompIndex", "Relay_SPST_StandexMeder_MS_Form1AB")

newPart.addTag("kicadDesc", "Standex-Meder MS SIL-relais, Form 1A/1B, see https://standexelectronics.com/de/produkte/ms-reed-relais/")
newPart.addTag("kicadTags", "Standex Meder MS SIL reed relais")
newPart.addTag("kicadAttr", "through_hole")
newPart.addTag("kicad3DModel", "${KICAD6_3DMODEL_DIR}/Relay_THT.3dshapes/Relay_SPST_StandexMeder_MS_Form1AB.wrl")

OOMP.parts.append(newPart)