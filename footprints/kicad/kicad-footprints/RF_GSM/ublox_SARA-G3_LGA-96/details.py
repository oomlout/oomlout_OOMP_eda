###### OOMP FILE  ######

import OOMP

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "kicad")
newPart.addTag("oompColor", "kicad-footprints")
newPart.addTag("oompDesc", "RF_GSM")
newPart.addTag("oompIndex", "ublox_SARA-G3_LGA-96")

newPart.addTag("kicadDesc", "ublox Sara GSM/HSPA modem, https://www.u-blox.com/sites/default/files/SARA-G3-U2_SysIntegrManual_%28UBX-13000995%29.pdf, pag.162")
newPart.addTag("kicadTags", "ublox SARA-G3 SARA-U2 GSM HSPA")
newPart.addTag("kicadAttr", "smd")
newPart.addTag("kicad3DModel", "${KICAD6_3DMODEL_DIR}/RF_GSM.3dshapes/ublox_SARA-G3_LGA-96.wrl")

OOMP.parts.append(newPart)