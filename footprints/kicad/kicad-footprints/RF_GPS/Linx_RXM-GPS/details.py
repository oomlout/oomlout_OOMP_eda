###### OOMP FILE  ######

import OOMP

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "kicad")
newPart.addTag("oompColor", "kicad-footprints")
newPart.addTag("oompDesc", "RF_GPS")
newPart.addTag("oompIndex", "Linx_RXM-GPS")

newPart.addTag("kicadDesc", "GPS Module, Linx (https://linxtechnologies.com/wp/wp-content/uploads/rxm-gps-rm.pdf)")
newPart.addTag("kicadTags", "gps linx")
newPart.addTag("kicadAttr", "smd")
newPart.addTag("kicad3DModel", "${KICAD6_3DMODEL_DIR}/RF_GPS.3dshapes/Linx_RXM-GPS.wrl")

OOMP.parts.append(newPart)