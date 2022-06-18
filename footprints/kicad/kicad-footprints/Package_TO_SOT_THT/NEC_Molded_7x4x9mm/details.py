###### OOMP FILE  ######

import OOMP

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "kicad")
newPart.addTag("oompColor", "kicad-footprints")
newPart.addTag("oompDesc", "Package_TO_SOT_THT")
newPart.addTag("oompIndex", "NEC_Molded_7x4x9mm")

newPart.addTag("kicadDesc", "Molded Japan Transistor Package 7x4x9mm^3, http://rtellason.com/transdata/2sb734.pdf")
newPart.addTag("kicadTags", "Japan transistor")
newPart.addTag("kicadAttr", "through_hole")
newPart.addTag("kicad3DModel", "${KICAD6_3DMODEL_DIR}/Package_TO_SOT_THT.3dshapes/NEC_Molded_7x4x9mm.wrl")

OOMP.parts.append(newPart)