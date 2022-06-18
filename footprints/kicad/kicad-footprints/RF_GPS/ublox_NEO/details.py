###### OOMP FILE  ######

import OOMP

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "kicad")
newPart.addTag("oompColor", "kicad-footprints")
newPart.addTag("oompDesc", "RF_GPS")
newPart.addTag("oompIndex", "ublox_NEO")

newPart.addTag("kicadDesc", "ublox NEO 6/7/8, (https://www.u-blox.com/sites/default/files/NEO-8Q-NEO-M8-FW3_HardwareIntegrationManual_%28UBX-15029985%29_0.pdf)")
newPart.addTag("kicadTags", "GPS ublox NEO 6/7/8")
newPart.addTag("kicadAttr", "smd")
newPart.addTag("kicad3DModel", "${KICAD6_3DMODEL_DIR}/RF_GPS.3dshapes/ublox_NEO.wrl")

OOMP.parts.append(newPart)