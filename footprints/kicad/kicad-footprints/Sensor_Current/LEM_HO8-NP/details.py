###### OOMP FILE  ######

import OOMP

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "kicad")
newPart.addTag("oompColor", "kicad-footprints")
newPart.addTag("oompDesc", "Sensor_Current")
newPart.addTag("oompIndex", "LEM_HO8-NP")

newPart.addTag("kicadDesc", "LEM HO 8/15/25-NP Current Transducer (https://www.lem.com/sites/default/files/products_datasheets/ho-np-0000_series.pdf)")
newPart.addTag("kicadTags", "current transducer")
newPart.addTag("kicadAttr", "through_hole")
newPart.addTag("kicad3DModel", "${KICAD6_3DMODEL_DIR}/Sensor_Current.3dshapes/LEM_HO8-NP.wrl")

OOMP.parts.append(newPart)