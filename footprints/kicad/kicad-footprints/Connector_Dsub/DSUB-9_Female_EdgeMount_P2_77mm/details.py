###### OOMP FILE  ######

import OOMP

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "kicad")
newPart.addTag("oompColor", "kicad-footprints")
newPart.addTag("oompDesc", "Connector_Dsub")
newPart.addTag("oompIndex", "DSUB-9_Female_EdgeMount_P2.77mm")

newPart.addTag("kicadDesc", "9-pin D-Sub connector, solder-cups edge-mounted, female, x-pin-pitch 2.77mm, distance of mounting holes 25mm, see https://disti-assets.s3.amazonaws.com/tonar/files/datasheets/16730.pdf")
newPart.addTag("kicadTags", "9-pin D-Sub connector edge mount solder cup female x-pin-pitch 2.77mm mounting holes distance 25mm")
newPart.addTag("kicadAttr", "smd")
newPart.addTag("kicad3DModel", "${KICAD6_3DMODEL_DIR}/Connector_Dsub.3dshapes/DSUB-9_Female_EdgeMount_P2.77mm.wrl")

OOMP.parts.append(newPart)