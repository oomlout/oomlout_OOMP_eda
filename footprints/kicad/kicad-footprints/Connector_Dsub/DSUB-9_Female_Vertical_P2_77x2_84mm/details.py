###### OOMP FILE  ######

import OOMP

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "kicad")
newPart.addTag("oompColor", "kicad-footprints")
newPart.addTag("oompDesc", "Connector_Dsub")
newPart.addTag("oompIndex", "DSUB-9_Female_Vertical_P2.77x2.84mm")

newPart.addTag("kicadDesc", "9-pin D-Sub connector, straight/vertical, THT-mount, female, pitch 2.77x2.84mm, distance of mounting holes 25mm, see https://disti-assets.s3.amazonaws.com/tonar/files/datasheets/16730.pdf")
newPart.addTag("kicadTags", "9-pin D-Sub connector straight vertical THT female pitch 2.77x2.84mm mounting holes distance 25mm")
newPart.addTag("kicadAttr", "through_hole")
newPart.addTag("kicad3DModel", "${KICAD6_3DMODEL_DIR}/Connector_Dsub.3dshapes/DSUB-9_Female_Vertical_P2.77x2.84mm.wrl")

OOMP.parts.append(newPart)