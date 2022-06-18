###### OOMP FILE  ######

import OOMP

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "kicad")
newPart.addTag("oompColor", "kicad-footprints")
newPart.addTag("oompDesc", "Inductor_THT")
newPart.addTag("oompIndex", "L_CommonMode_Wuerth_WE-CMB-L")

newPart.addTag("kicadDesc", "Wuerth, WE-CMB, Bauform L,")
newPart.addTag("kicadTags", "CommonModeChoke Gleichtaktdrossel")
newPart.addTag("kicadAttr", "through_hole")
newPart.addTag("kicad3DModel", "${KICAD6_3DMODEL_DIR}/Inductor_THT.3dshapes/L_CommonMode_Wuerth_WE-CMB-L.wrl")

OOMP.parts.append(newPart)