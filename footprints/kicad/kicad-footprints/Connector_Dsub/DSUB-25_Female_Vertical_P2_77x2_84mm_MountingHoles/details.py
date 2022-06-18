###### OOMP FILE  ######

import OOMP

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "kicad")
newPart.addTag("oompColor", "kicad-footprints")
newPart.addTag("oompDesc", "Connector_Dsub")
newPart.addTag("oompIndex", "DSUB-25_Female_Vertical_P2.77x2.84mm_MountingHoles")

newPart.addTag("kicadDesc", "25-pin D-Sub connector, straight/vertical, THT-mount, female, pitch 2.77x2.84mm, distance of mounting holes 47.1mm, see https://disti-assets.s3.amazonaws.com/tonar/files/datasheets/16730.pdf")
newPart.addTag("kicadTags", "25-pin D-Sub connector straight vertical THT female pitch 2.77x2.84mm mounting holes distance 47.1mm")
newPart.addTag("kicadAttr", "through_hole")
newPart.addTag("kicad3DModel", "${KICAD6_3DMODEL_DIR}/Connector_Dsub.3dshapes/DSUB-25_Female_Vertical_P2.77x2.84mm_MountingHoles.wrl")

OOMP.parts.append(newPart)