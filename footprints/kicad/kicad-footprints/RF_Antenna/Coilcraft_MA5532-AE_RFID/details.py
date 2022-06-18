###### OOMP FILE  ######

import OOMP

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "kicad")
newPart.addTag("oompColor", "kicad-footprints")
newPart.addTag("oompDesc", "RF_Antenna")
newPart.addTag("oompIndex", "Coilcraft_MA5532-AE_RFID")

newPart.addTag("kicadDesc", "RFID Transponder Coil")
newPart.addTag("kicadTags", "antenna rfid coilcraft")
newPart.addTag("kicadAttr", "smd")
newPart.addTag("kicad3DModel", "${KICAD6_3DMODEL_DIR}/RF_Antenna.3dshapes/Coilcraft_MA5532-AE_RFID.wrl")

OOMP.parts.append(newPart)