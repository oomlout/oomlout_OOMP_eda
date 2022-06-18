###### OOMP FILE  ######

import OOMP

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "kicad")
newPart.addTag("oompColor", "kicad-footprints")
newPart.addTag("oompDesc", "RF_GPS")
newPart.addTag("oompIndex", "ublox_MAX")
newPart.addTag("oompName", "kicad-footprints/RF_GPS/ublox_MAX")

newPart.addTag("kicadDesc", "ublox MAX 6/7/8, (https://www.u-blox.com/sites/default/files/MAX-8-M8-FW3_HardwareIntegrationManual_%28UBX-15030059%29.pdf)")
newPart.addTag("kicadTags", "GPS ublox MAX 6/7/8")
newPart.addTag("kicadAttr", "smd")
newPart.addTag("kicad3DModel", "${KICAD6_3DMODEL_DIR}/RF_GPS.3dshapes/ublox_MAX.wrl")

OOMP.parts.append(newPart)