###### OOMP FILE  ######

import OOMP

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "kicad")
newPart.addTag("oompColor", "kicad-footprints")
newPart.addTag("oompDesc", "Sensor_Current")
newPart.addTag("oompIndex", "LEM_HTFS")

newPart.addTag("kicadDesc", "LEM HTFS x00-P current transducer (https://www.lem.com/sites/default/files/products_datasheets/htfs_200_800-p.pdf)")
newPart.addTag("kicadTags", "HTFS current transducer")
newPart.addTag("kicadAttr", "through_hole")
newPart.addTag("kicad3DModel", "${KICAD6_3DMODEL_DIR}/Sensor_Current.3dshapes/LEM_HTFS.wrl")

OOMP.parts.append(newPart)