###### OOMP FILE  ######

import OOMP

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "kicad")
newPart.addTag("oompColor", "kicad-footprints")
newPart.addTag("oompDesc", "Transformer_THT")
newPart.addTag("oompIndex", "Transformer_Breve_TEZ-22x24")

newPart.addTag("kicadDesc", "http://www.breve.pl/pdf/ANG/TEZ_ang.pdf")
newPart.addTag("kicadTags", "TEZ PCB Transformer")
newPart.addTag("kicadAttr", "through_hole")
newPart.addTag("kicad3DModel", "${KICAD6_3DMODEL_DIR}/Transformer_THT.3dshapes/Transformer_Breve_TEZ-22x24.wrl")

OOMP.parts.append(newPart)