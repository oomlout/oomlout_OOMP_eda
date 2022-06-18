###### OOMP FILE  ######

import OOMP

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "kicad")
newPart.addTag("oompColor", "kicad-footprints")
newPart.addTag("oompDesc", "Connector_Dsub")
newPart.addTag("oompIndex", "DSUB-37_Male_EdgeMount_P2.77mm")

newPart.addTag("kicadDesc", "37-pin D-Sub connector, solder-cups edge-mounted, male, x-pin-pitch 2.77mm, distance of mounting holes 63.5mm, see https://disti-assets.s3.amazonaws.com/tonar/files/datasheets/16730.pdf")
newPart.addTag("kicadTags", "37-pin D-Sub connector edge mount solder cup male x-pin-pitch 2.77mm mounting holes distance 63.5mm")
newPart.addTag("kicadAttr", "smd")
newPart.addTag("kicad3DModel", "${KICAD6_3DMODEL_DIR}/Connector_Dsub.3dshapes/DSUB-37_Male_EdgeMount_P2.77mm.wrl")

OOMP.parts.append(newPart)