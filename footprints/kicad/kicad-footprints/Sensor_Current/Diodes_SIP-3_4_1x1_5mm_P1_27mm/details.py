###### OOMP FILE  ######

import OOMP

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "kicad")
newPart.addTag("oompColor", "kicad-footprints")
newPart.addTag("oompDesc", "Sensor_Current")
newPart.addTag("oompIndex", "Diodes_SIP-3_4.1x1.5mm_P1.27mm")

newPart.addTag("kicadDesc", "Diodes SIP-3 Bulk Pack, 1.27mm Pitch (https://www.diodes.com/assets/Package-Files/SIP-3-Bulk-Pack.pdf)")
newPart.addTag("kicadTags", "Diodes SIP-3 Bulk Pack")
newPart.addTag("kicadAttr", "through_hole")
newPart.addTag("kicad3DModel", "${KICAD6_3DMODEL_DIR}/Sensor_Current.3dshapes/Diodes_SIP-3_4.1x1.5mm_P1.27mm.wrl")

OOMP.parts.append(newPart)