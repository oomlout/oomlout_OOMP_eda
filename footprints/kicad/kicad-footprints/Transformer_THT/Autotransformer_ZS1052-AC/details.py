###### OOMP FILE  ######

import OOMP

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "kicad")
newPart.addTag("oompColor", "kicad-footprints")
newPart.addTag("oompDesc", "Transformer_THT")
newPart.addTag("oompIndex", "Autotransformer_ZS1052-AC")

newPart.addTag("kicadDesc", "Ignition coil for xenon flash, http://www.excelitas.com/downloads/ZS1052ACH.pdf")
newPart.addTag("kicadTags", "ignition coil autotransformer")
newPart.addTag("kicadAttr", "through_hole")
newPart.addTag("kicad3DModel", "${KICAD6_3DMODEL_DIR}/Transformer_THT.3dshapes/Autotransformer_ZS1052-AC.wrl")

OOMP.parts.append(newPart)