###### OOMP FILE  ######

import OOMP

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "kicad")
newPart.addTag("oompColor", "kicad-footprints")
newPart.addTag("oompDesc", "RF_GPS")
newPart.addTag("oompIndex", "ublox_ZED")
newPart.addTag("oompName", "kicad-footprints/RF_GPS/ublox_ZED")

newPart.addTag("kicadDesc", "ublox ZED-F9, https://www.u-blox.com/sites/default/files/ZED-F9P_DataSheet_%28UBX-17051259%29.pdf")
newPart.addTag("kicadTags", "GPS GNSS ublox ZED")
newPart.addTag("kicadAttr", "smd")
newPart.addTag("kicad3DModel", "${KICAD6_3DMODEL_DIR}/RF_GPS.3dshapes/ublox_ZED.wrl")

OOMP.parts.append(newPart)