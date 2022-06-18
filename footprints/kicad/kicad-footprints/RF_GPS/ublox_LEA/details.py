###### OOMP FILE  ######

import OOMP

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "kicad")
newPart.addTag("oompColor", "kicad-footprints")
newPart.addTag("oompDesc", "RF_GPS")
newPart.addTag("oompIndex", "ublox_LEA")
newPart.addTag("oompName", "kicad-footprints/RF_GPS/ublox_LEA")

newPart.addTag("kicadDesc", "ublox LEA 6/7/8, (https://www.u-blox.com/sites/default/files/LEA-M8S-M8T-FW3_HardwareIntegrationManual_%28UBX-15030060%29.pdf)")
newPart.addTag("kicadTags", "GPS ublox LEA 6/7/8")
newPart.addTag("kicadAttr", "smd")
newPart.addTag("kicad3DModel", "${KICAD6_3DMODEL_DIR}/RF_GPS.3dshapes/ublox_LEA.wrl")

OOMP.parts.append(newPart)