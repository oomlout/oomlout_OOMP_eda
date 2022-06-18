###### OOMP FILE  ######

import OOMP

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "kicad")
newPart.addTag("oompColor", "kicad-footprints")
newPart.addTag("oompDesc", "Connector_Dsub")
newPart.addTag("oompIndex", "DSUB-44-HD_Female_Vertical_P2.29x1.98mm_MountingHoles")

newPart.addTag("kicadDesc", "44-pin D-Sub connector, straight/vertical, THT-mount, female, pitch 2.29x1.98mm, distance of mounting holes 47.1mm, see https://disti-assets.s3.amazonaws.com/tonar/files/datasheets/16730.pdf")
newPart.addTag("kicadTags", "44-pin D-Sub connector straight vertical THT female pitch 2.29x1.98mm mounting holes distance 47.1mm")
newPart.addTag("kicadAttr", "through_hole")
newPart.addTag("kicad3DModel", "${KICAD6_3DMODEL_DIR}/Connector_Dsub.3dshapes/DSUB-44-HD_Female_Vertical_P2.29x1.98mm_MountingHoles.wrl")

OOMP.parts.append(newPart)