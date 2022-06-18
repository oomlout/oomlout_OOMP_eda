###### OOMP FILE  ######

import OOMP

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "kicad")
newPart.addTag("oompColor", "kicad-footprints")
newPart.addTag("oompDesc", "Sensor_Humidity")
newPart.addTag("oompIndex", "Sensirion_DFN-4-1EP_2x2mm_P1mm_EP0.7x1.6mm")

newPart.addTag("kicadDesc", "DFN, 4 Pin (https://www.sensirion.com/fileadmin/user_upload/customers/sensirion/Dokumente/0_Datasheets/Humidity/Sensirion_Humidity_Sensors_SHTC3_Datasheet.pdf)")
newPart.addTag("kicadTags", "Sensirion DFN NoLead")
newPart.addTag("kicadAttr", "smd")
newPart.addTag("kicad3DModel", "${KICAD6_3DMODEL_DIR}/Sensor_Humidity.3dshapes/Sensirion_DFN-4-1EP_2x2mm_P1mm_EP0.7x1.6mm.wrl")

OOMP.parts.append(newPart)