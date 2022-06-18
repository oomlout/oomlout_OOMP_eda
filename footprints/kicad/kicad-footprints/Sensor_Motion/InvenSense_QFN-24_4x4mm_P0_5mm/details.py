###### OOMP FILE  ######

import OOMP

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "kicad")
newPart.addTag("oompColor", "kicad-footprints")
newPart.addTag("oompDesc", "Sensor_Motion")
newPart.addTag("oompIndex", "InvenSense_QFN-24_4x4mm_P0.5mm")

newPart.addTag("kicadDesc", "24-Lead Plastic QFN (4mm x 4mm); Pitch 0.5mm; EP 2.7x2.6mm; for InvenSense motion sensors; keepout area marked (Package see: https://store.invensense.com/datasheets/invensense/MPU-6050_DataSheet_V3%204.pdf; See also https://www.invensense.com/wp-content/uploads/2015/02/InvenSense-MEMS-Handling.pdf)")
newPart.addTag("kicadTags", "QFN 0.5")
newPart.addTag("kicadAttr", "smd")
newPart.addTag("kicad3DModel", "${KICAD6_3DMODEL_DIR}/Package_DFN_QFN.3dshapes/QFN-24-1EP_4x4mm_P0.5mm_EP2.7x2.6mm.wrl")

OOMP.parts.append(newPart)