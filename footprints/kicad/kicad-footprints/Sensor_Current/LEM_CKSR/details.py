###### OOMP FILE  ######

import OOMP

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "kicad")
newPart.addTag("oompColor", "kicad-footprints")
newPart.addTag("oompDesc", "Sensor_Current")
newPart.addTag("oompIndex", "LEM_CKSR")

newPart.addTag("kicadDesc", "LEM CKSR 6/15/25/50/75-NP Current Transducer, https://www.lem.com/sites/default/files/products_datasheets/cksr_75-np.pdf")
newPart.addTag("kicadTags", "current transducer LEM")
newPart.addTag("kicadAttr", "through_hole")
newPart.addTag("kicad3DModel", "${KICAD6_3DMODEL_DIR}/Sensor_Current.3dshapes/LEM_CKSR.wrl")

OOMP.parts.append(newPart)