###### OOMP FILE  ######

import OOMP

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "kicad")
newPart.addTag("oompColor", "kicad-footprints")
newPart.addTag("oompDesc", "Package_TO_SOT_SMD")
newPart.addTag("oompIndex", "TSOT-23_HandSoldering")

newPart.addTag("kicadDesc", "5-pin TSOT23 package, http://cds.linear.com/docs/en/packaging/SOT_5_05-08-1635.pdf")
newPart.addTag("kicadTags", "TSOT-23 Hand-soldering")
newPart.addTag("kicadAttr", "smd")
newPart.addTag("kicad3DModel", "${KICAD6_3DMODEL_DIR}/Package_TO_SOT_SMD.3dshapes/TSOT-23.wrl")

OOMP.parts.append(newPart)