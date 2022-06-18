###### OOMP FILE  ######

import OOMP

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "kicad")
newPart.addTag("oompColor", "kicad-footprints")
newPart.addTag("oompDesc", "Relay_THT")
newPart.addTag("oompIndex", "Relay_SPDT_Schrack-RT1-16A-FormC_RM5mm")

newPart.addTag("kicadDesc", "Relay SPST Schrack-RT1 RM5mm 16A 250V AC Form C http://image.schrack.com/datenblaetter/h_rt114012--_de.pdf")
newPart.addTag("kicadTags", "Relay SPST Schrack-RT1 RM5mm 16A 250V AC Relay")
newPart.addTag("kicadAttr", "through_hole")
newPart.addTag("kicad3DModel", "${KICAD6_3DMODEL_DIR}/Relay_THT.3dshapes/Relay_DPDT_Schrack-RT2-FormC_RM5mm.wrl")

OOMP.parts.append(newPart)