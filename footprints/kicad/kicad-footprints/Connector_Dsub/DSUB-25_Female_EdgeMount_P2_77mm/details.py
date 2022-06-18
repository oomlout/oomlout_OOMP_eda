###### OOMP FILE  ######

import OOMP

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "kicad")
newPart.addTag("oompColor", "kicad-footprints")
newPart.addTag("oompDesc", "Connector_Dsub")
newPart.addTag("oompIndex", "DSUB-25_Female_EdgeMount_P2.77mm")
newPart.addTag("oompName", "kicad-footprints/Connector_Dsub/DSUB-25_Female_EdgeMount_P2.77mm")

newPart.addTag("kicadDesc", "25-pin D-Sub connector, solder-cups edge-mounted, female, x-pin-pitch 2.77mm, distance of mounting holes 47.1mm, see https://disti-assets.s3.amazonaws.com/tonar/files/datasheets/16730.pdf")
newPart.addTag("kicadTags", "25-pin D-Sub connector edge mount solder cup female x-pin-pitch 2.77mm mounting holes distance 47.1mm")
newPart.addTag("kicadAttr", "smd")
newPart.addTag("kicad3DModel", "${KICAD6_3DMODEL_DIR}/Connector_Dsub.3dshapes/DSUB-25_Female_EdgeMount_P2.77mm.wrl")

OOMP.parts.append(newPart)