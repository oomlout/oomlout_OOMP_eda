###### OOMP FILE  ######

import OOMP

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "kicad")
newPart.addTag("oompColor", "kicad-footprints")
newPart.addTag("oompDesc", "Sensor_Motion")
newPart.addTag("oompIndex", "InvenSense_QFN-24_3x3mm_P0.4mm")

newPart.addTag("kicadDesc", "24-Lead Plastic QFN (3mm x 3mm); Pitch 0.4mm; EP 1.7x1.54mm; for InvenSense motion sensors; keepout area marked (Package see: https://store.invensense.com/datasheets/invensense/MPU9250REV1.0.pdf; See also https://www.invensense.com/wp-content/uploads/2015/02/InvenSense-MEMS-Handling.pdf)")
newPart.addTag("kicadTags", "QFN 0.4")
newPart.addTag("kicadAttr", "smd")
newPart.addTag("kicad3DModel", "${KICAD6_3DMODEL_DIR}/Package_DFN_QFN.3dshapes/QFN-24_3x3mm_P0.4mm_EP1.7x1.54mm.wrl")

OOMP.parts.append(newPart)