###### OOMP FILE  ######

import OOMP

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "kicad")
newPart.addTag("oompColor", "kicad-footprints")
newPart.addTag("oompDesc", "Package_TO_SOT_THT")
newPart.addTag("oompIndex", "SOD-70_P2.54mm")

newPart.addTag("kicadDesc", "Plastic near cylindrical package Sod-70 see: https://www.nxp.com/docs/en/data-sheet/KTY81_SER.pdf  [StepUp generated footprint]")
newPart.addTag("kicadTags", "Sod-70")
newPart.addTag("kicadAttr", "through_hole")
newPart.addTag("kicad3DModel", "${KICAD6_3DMODEL_DIR}/Package_TO_SOT_THT.3dshapes/SOD-70_P2.54mm.wrl")

OOMP.parts.append(newPart)