###### OOMP FILE  ######

import OOMP

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "kicad")
newPart.addTag("oompColor", "kicad-footprints")
newPart.addTag("oompDesc", "Package_TO_SOT_THT")
newPart.addTag("oompIndex", "TO-220-2_Vertical")

newPart.addTag("kicadDesc", "TO-220-2, Vertical, RM 5.08mm, see https://www.centralsemi.com/PDFS/CASE/TO-220-2PD.PDF")
newPart.addTag("kicadTags", "TO-220-2 Vertical RM 5.08mm")
newPart.addTag("kicadAttr", "through_hole")
newPart.addTag("kicad3DModel", "${KICAD6_3DMODEL_DIR}/Package_TO_SOT_THT.3dshapes/TO-220-2_Vertical.wrl")

OOMP.parts.append(newPart)