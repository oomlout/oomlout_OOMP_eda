###### OOMP FILE  ######

import OOMP

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "kicad")
newPart.addTag("oompColor", "kicad-footprints")
newPart.addTag("oompDesc", "Sensor_Voltage")
newPart.addTag("oompIndex", "LEM_LV25-P")
newPart.addTag("oompName", "kicad-footprints/Sensor_Voltage/LEM_LV25-P")

newPart.addTag("kicadDesc", "LEM LV25-P Voltage transducer, https://www.lem.com/sites/default/files/products_datasheets/lv_25-p.pdf")
newPart.addTag("kicadTags", "LEM Hall Effect Voltage transducer")
newPart.addTag("kicadAttr", "through_hole")
newPart.addTag("kicad3DModel", "${KICAD6_3DMODEL_DIR}/Sensor_Voltage.3dshapes/LEM_LV25-P.wrl")

OOMP.parts.append(newPart)