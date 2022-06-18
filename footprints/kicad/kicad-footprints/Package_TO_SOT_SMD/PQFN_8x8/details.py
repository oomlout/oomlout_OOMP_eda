###### OOMP FILE  ######

import OOMP

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "kicad")
newPart.addTag("oompColor", "kicad-footprints")
newPart.addTag("oompDesc", "Package_TO_SOT_SMD")
newPart.addTag("oompIndex", "PQFN_8x8")
newPart.addTag("oompName", "kicad-footprints/Package_TO_SOT_SMD/PQFN_8x8")

newPart.addTag("kicadDesc", "Low Profile 8x8mm PQFN, Dual Cool 88, https://www.onsemi.com/pub/Collateral/FDMT80080DC-D.pdf")
newPart.addTag("kicadTags", "pqfn vdfn mosfet")
newPart.addTag("kicadAttr", "smd")
newPart.addTag("kicad3DModel", "${KICAD6_3DMODEL_DIR}/Package_TO_SOT_SMD.3dshapes/PQFN_8x8.wrl")

OOMP.parts.append(newPart)